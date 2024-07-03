from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    user = models.Foreign & Key(User, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    settings = models.JSONField(default=dict)
