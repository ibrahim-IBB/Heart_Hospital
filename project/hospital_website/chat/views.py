from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.http import HttpResponse
from .forms import MailForm
from mainapp.models import Mail
from django.core.mail import send_mail
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



def mail_form(request):

    if request.method=='POST':
        form=MailForm(request.POST)
        if form.is_valid():
            mail=Mail.objects.create(user=request.user,email_reply=form.cleaned_data['email_reply'])
            
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['content'],
                recipient_list=['codibsod500@gmail.com'],
                fail_silently=False,
                from_email=None
            )

            mail.save()
            return HttpResponse("Form submitted successfully.")
    else:
        form=MailForm()
        
    return render(request,'chat/mails.html',{"form":form})
