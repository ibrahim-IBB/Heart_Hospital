from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
# Create your views here.
@login_required
def home(request,room=None):
    rooms=Room.objects.all()

    try:
        active_room=Room.objects.get(slug=room)
    except Room.DoesNotExist:
        active_room=None
    return render(request,"chat/base.html",context={"rooms":rooms,"active_room":active_room})