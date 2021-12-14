from rest_framework import serializers

from user_messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        # fields = ['text', 'created_at']
        fields = '__all__'
