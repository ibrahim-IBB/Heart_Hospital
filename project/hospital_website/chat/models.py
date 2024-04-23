from django.db import models
from django.conf import settings
# Create your models here.


class Room(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    


class Message(models.Model):
    message_text=models.TextField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    room=models.SlugField()