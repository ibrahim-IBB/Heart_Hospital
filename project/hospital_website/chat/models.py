from django.db import models
from django.conf import settings

from django.conf import settings
# Create your models here.


class Room(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    


class Message(models.Model):
    content=models.TextField()
    user=models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="messages")
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="messages")
    date_added=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('date_added',)


