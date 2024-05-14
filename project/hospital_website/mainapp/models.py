from django.db import models
""" from django.utils import timezone
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html """
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from html import escape

# Create your models here.


def escape_except_br(text):
    # Replace <br> with a placeholder
    text = text.replace('<br>', 'PLACEHOLDER_BR')
    
    # Escape the HTML
    escaped_text =escape(text, quote=True)
    
    # Replace the placeholder with <br> again
    escaped_text = escaped_text.replace('PLACEHOLDER_BR', '<br>')
    
    return escaped_text


help_subject_tags=escape_except_br(
    '''
text item:<br><br>
      <div class="text_item"><br>
         نص للتجربة<br>
        </div>       <br>   <br>                      
multi_image (اكثر من صورة):<br><br>
          <div class="multi_image_item"><br>
            <img src="3" alt=""><br>
            <img src="2" alt=""><br>
            <img src="1" alt=""><br>
        </div><br><br>
image_item (صورة واحدة):<br><br>
                                     
           <div class="image_item"><br>
            <img src="1" alt=""><br>
        </div>                           
''')

class Subject(models.Model):
    sub_subjects=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    main_title=models.CharField(unique=True,max_length=100,null=True,blank=True)
    title=models.CharField(max_length=500)
    main_image=models.ImageField(upload_to="images/",blank=True,null=True)  
    subject_contnet=models.TextField(default=" ",help_text=help_subject_tags)

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
    image=models.ImageField(upload_to="sub_images/%Y/%m/%d")


    def __str__(self):
        return self.image.url




class report(models.Model):
    title=models.CharField(max_length=250)
    report_content=models.TextField(default=" ")
    image=models.ImageField(upload_to="reports/%Y/%m/%d",null=True,blank=True)
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
    image=models.ImageField(default="/default.jpg",upload_to="profile/%Y/%m/%d")
    

    phone_number = models.CharField(max_length=60,
                             null=True, blank=True)
    
    birthdate=models.DateField(blank=True,null=True)



    def __str__(self):
        return f"{self.user.username} Profile"


class Mail(models.Model):
    email_reply=models.CharField(max_length=255)
    subject=models.CharField(max_length=255,null=False,default='')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    email_body=RichTextUploadingField(null=True,blank=True)
    user_visible=models.BooleanField(default=True)
    replied=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.subject
    



class Doctor(models.Model):
    register_time=models.DateTimeField(auto_now=True,blank=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    number=models.CharField(max_length=15)
    job_title=models.CharField(max_length=255)
    image=models.ImageField(default="/default.jpg",upload_to="doctor/%Y/%m/%d")
    def __str__(self):
        return self.first_name+" "+self.last_name

