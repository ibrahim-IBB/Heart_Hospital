from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from django.http import HttpResponse
from .forms import MailForm
from mainapp.models import Mail
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from smtplib import SMTPException
from django.contrib.auth.models import User,Group
from django.conf import settings
from django.db.models  import Q

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



def mail_form(request,reply=None):

    to=None
    admin=False # False mean using default email which is defined  in the settings
    successfully_send=True

    if request.user.groups.filter(name='employees').exists():
            
            admin=True
    else:

        admin=False

        


    #if the user is the admin and there is no slug=reply to reply to a mail then go to list emails
    if admin and reply==None:
        return redirect('emails_list')
    if request.method=='POST':


        
        form=MailForm(request.POST)
        if form.is_valid():

            try:
                cnform=form.cleaned_data
                
                if admin and reply !=None:
                    to=User.objects.get(username=reply).email
                else:
                    to=settings.EMAIL_HOST_USER# get default email of website(hospital)
                msg=EmailMultiAlternatives(
                subject=cnform['subject'],
                body=strip_tags(cnform['content']),
                to=[to,],
                from_email=None,
                )
                
                msg.attach_alternative(cnform['content'], "text/html")
                
                msg.send()
                
                
                mail=Mail.objects.create(user=request.user,email_reply=to,
                                         subject=cnform['subject'],
                                         email_body=cnform['content'])
                #mail.save()
            except SMTPException as e:
                print("error sending mail ")
                print(e)
                successfully_send=False

            # save email if submitted successfully
            if successfully_send:
                mail.save()    

                return redirect('main')
        

    else:
        form=MailForm()
        
    return render(request,'chat/mails.html',{"form":form,'reply':to})


def emails_list(request):
    active_user_mails=Q(user=request.user)
    admin_user_mails=Q(user=User.objects.get(is_superuser=True))
    

    if request.user.is_superuser:
        q1=Q(user=request.user)
        q2=Q(email_reply='hospital@gmail.com')
        emails=Mail.objects.filter(q1 | q2).order_by('created')
    else:


        emails=Mail.objects.filter(admin_user_mails | active_user_mails)
        
    


    return render(request,'chat/mails_list.html',{'emails':emails})


def show_email(request,mail_id):

    mail=Mail.objects.get(id=mail_id)
    reply_link=False
    if request.user.is_superuser and mail.user != request.user:
        reply_link=True
    
    

    return render(request,'chat/mail_show.html',context={'mail':mail,'reply_link':reply_link})