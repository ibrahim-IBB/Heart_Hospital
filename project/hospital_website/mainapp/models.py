from django.db import models
""" from django.utils import timezone
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html """
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.



class Subject(models.Model):
    sub_subjects=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    main_title=models.CharField(unique=True,max_length=100,null=True,blank=True)
    title=models.CharField(max_length=500)
    main_image=models.ImageField(upload_to="images/",blank=True,null=True)  
    subject_contnet=models.TextField(default=" ")

    def main_title_en(self):
        if self.main_title =='المرضى و الزوار':
            return "patients_and_visitors"
        elif self.main_title ==  "خدمات المستشفى":
            return "hospital_services"
        elif self.main_title == "حول المستشفى":
            return "about_hospital"
        
    #to check what type of model is inside html template language
    def return_type(self):
        return "subject" 
    
  
    def __str__(self):
        return self.title



class subject_image(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="images/sub_images")




class report(models.Model):
    title=models.CharField(max_length=250)
    report_content=models.TextField(default=" ")
    image=models.ImageField(upload_to="images/reports/",null=True,blank=True)
    created=models.DateTimeField(auto_now=True,blank=True)

    #to check what type of model is inside html template language
    def return_type(self):
        return "report"

    def __str__(self):
        return self.title
    


class Testing(models.Model):
    name=models.CharField(max_length=255)
    sub_test=models.ForeignKey("self",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user=models.OneToOneField( settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.ImageField(default="/profile_pics/default.jpg",upload_to="profile_pics")


    phone_number = models.CharField(max_length=60,
                             null=True, blank=True)
    
    birthdate=models.DateField(blank=True,null=True)



    def __str__(self):
        return f"{self.user.username} Profile"