from django.urls import path

from . import views
urlpatterns=[
path('mail_send/<slug:reply>/',views.mail_form,name="mail_form"),
path('mail_send/',views.mail_form,name="mail_form"),
path("chat/<slug:room>/",views.home,name='base_chat'),  
path("",views.home,name='base_chat'), 
path("mail/emails_list/",views.emails_list,name="emails_list"),
path("mail/mail_show/<int:mail_id>/",views.show_email,name="mail_show")
]