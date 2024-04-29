from django.urls import path

from . import views
urlpatterns=[
path('mail_send/',views.mail_form,name="mail_form"),
    path("chat/<slug:room>/",views.home,name='base_chat'),  
path("",views.home,name='base_chat'), 

]