from django.urls import path

from . import views
urlpatterns=[
    path("",views.main),  
    path("about_hospital/",views.about_hospital),
    path("about_hospital/<int:subject_id>/",views.about_hospital),
    path("hospital_services/",views.hospital_services),
    path("hospital_services/<int:subject_id>/",views.hospital_services),
    path("patients_and_visitors/",views.patients_and_visitors),
    path("patients_and_visitors/<int:subject_id>/",views.patients_and_visitors),
    path("reports/<int:page>/",views.reports),
    path("report/<int:report_id>/",views.report_page),
    path("contact_info/",views.contact_info),
    path("search_result/",views.search)
    
]