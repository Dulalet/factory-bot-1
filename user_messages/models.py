import uuid as uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_user_model())


class Chat(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chatid = models.IntegerField(unique=True, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_user_model())
