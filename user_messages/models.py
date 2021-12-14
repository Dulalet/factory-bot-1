from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_user_model())
