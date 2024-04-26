from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Message
# Create your views here.
@login_required
def home(request,room=None):
    rooms=Room.objects.all()
    messages=None
    try:
        active_room=Room.objects.get(slug=room)
        messages=Message.objects.filter(room=active_room) 
    except Room.DoesNotExist:
        active_room=None
        messages=None
    return render(request,"chat/base.html",context={"rooms":rooms,"active_room":active_room,'messages':messages})