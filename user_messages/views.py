import telegram

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from bot.bot_settings import BOT_API_TOKEN
from user_messages.models import Chat, Message
from user_messages.serializers import MessageSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def send_message(request):
    serialized = MessageSerializer(data=request.data)
    if serialized.is_valid():
        chatqs = Chat.objects.filter(user=request.user)
        if chatqs:
            bot = telegram.Bot(token=BOT_API_TOKEN)
            bot.sendMessage(chat_id=chatqs[0].chatid, text=serialized.validated_data['text'])

            msg = Message()
            msg.user = request.user
            msg.text = serialized.validated_data['text']
            msg.save()
            return Response(HTTP_200_OK)
        else:
            return Response("please write to the bot first", HTTP_400_BAD_REQUEST)
    return Response("incorrect input", HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_messages_by_user(request):
    messages = Message.objects.filter(user=request.user)
    validated_messages = MessageSerializer(messages, many=True)
    return Response(validated_messages.data, HTTP_200_OK)
