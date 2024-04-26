from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
urlpatterns=[
    path("",views.main,name="main"),  
    
    #show the subject page after click on search result 
    path("subject/<int:subject_id>/",views.global_subject),

    path("about_hospital/",views.about_hospital,name="about_hospital"),
    path("about_hospital/<int:subject_id>/",views.about_hospital),
    path("hospital_services/",views.hospital_services),
    path("hospital_services/<int:subject_id>/",views.hospital_services),
    path("patients_and_visitors/",views.patients_and_visitors),
    path("patients_and_visitors/<int:subject_id>/",views.patients_and_visitors),
    path("reports/<int:page>/",views.reports),
    path("report/<int:report_id>/",views.report_page),
    path("contact_info/",views.contact_info),
    path("search_result/",views.search),
    path("subject_set_parent/<int:subject_id>/",views.subject_set_parent),
     path("subject_parent_remove/<int:subject_id>/",views.subject_parent_remove),
     path("subject_list/",views.subject_list),
    path("signup/",views.signup,name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="htmlFiles/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("profile/",views.profile,name="profile")
]