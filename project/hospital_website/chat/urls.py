from django.urls import path

from . import views
urlpatterns=[

    path("<slug:room>/",views.home,name='base_chat'),  
path("",views.home,name='base_chat'),  
]