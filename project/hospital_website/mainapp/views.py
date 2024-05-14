from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.http import Http404
from itertools import chain
from django.db.models  import Q
# Create your views here.
from .models import Subject,report,Profile,Doctor
from .froms import SignUpForm 



def contact_info(request):
    searched_doctors=None
    
    if request.GET.get('doctor'):

        q1=Q(job_title__icontains=request.GET['doctor'])
        q2=Q(first_name__icontains=request.GET['doctor'])
        q3=Q(last_name__icontains=request.GET['doctor'])
        searched_doctors=Doctor.objects.filter(q1|q2|q3)
    doctors=Doctor.objects.all()[:3]


    return render(request,"htmlFiles/contact_info.html",{'doctors':doctors,'searched_doctors':searched_doctors})

def main(request):

    recent_reports=report.objects.order_by('-created')[1:7]
   
    first_report=report.objects.order_by('-created').first()
    context={
        "recent_reports":recent_reports,
        "first_report":first_report
    }

    return render(request,"htmlfiles/main.html",context=context)



def news(request):

    return render(request,"htmlfiles/news.html")





def about_hospital(request,subject_id=None):

    # get the subject by id 
    sub_subjects=None
    if subject_id == None:
        subject_get=Subject.objects.get(main_title="حول المستشفى")
    else:
        subject_get=Subject.objects.get(pk=subject_id)
        print(subject_get)
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    #get the subject content and parse it to html
    soup=BeautifulSoup(subject_get.subject_contnet,"html.parser")
    #change all img src in the subject content to url  by replace the id number of image by url
    for img in soup.find_all("img"):
        img_url=subject_get.subject_image_set.get(id=int(img['src']) ).image.url 
        img['src']=img_url 

    context={
        "object":subject_get,
        "content":str(soup),
        "sub_subjects":sub_subjects
    }
   
    return render(request,"htmlFiles/about_hospital.html",context=context)








def hospital_services(request,subject_id=None):

    # get the subject by id 
    sub_subjects=None
    if subject_id == None:
        print("there is no id")

        subject_get=Subject.objects.get(main_title="خدمات المستشفى")
    else:
        print("id founded")
        subject_get=Subject.objects.get(pk=subject_id)
        print(subject_get)

    
    
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    
    print(sub_subjects)
    #get the subject content and parse it to html
    soup=BeautifulSoup(subject_get.subject_contnet,"html.parser")
    #change all img src in the subject content to url  by replace the id number of image by url
    for img in soup.find_all("img"):
        print(subject_get.subject_image_set.get(id=int(img['src']) ).image.url )
        img_url=subject_get.subject_image_set.get(id=int(img['src']) ).image.url 
        img['src']=img_url 

    context={
        "object":subject_get,
        "content":str(soup),
        "sub_subjects":sub_subjects
    }
   
    return render(request,"htmlFiles/hospital_services.html",context=context)





def patients_and_visitors(request,subject_id=None):

    # get the subject by id 
    sub_subjects=None
    if subject_id == None:
        print("there is no id")

        subject_get=Subject.objects.get(main_title="المرضى و الزوار")
    else:
        print("id founded")
        subject_get=Subject.objects.get(pk=subject_id)
        print(subject_get)

    
    
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    
    print(sub_subjects)
    #get the subject content and parse it to html
    soup=BeautifulSoup(subject_get.subject_contnet,"html.parser")
    #change all img src in the subject content to url  by replace the id number of image by url
    for img in soup.find_all("img"):
        print(subject_get.subject_image_set.get(id=int(img['src']) ).image.url )
        img_url=subject_get.subject_image_set.get(id=int(img['src']) ).image.url 
        img['src']=img_url 

    context={
        "object":subject_get,
        "content":str(soup),
        "sub_subjects":sub_subjects
    }
   
    return render(request,"htmlFiles/hospital_services.html",context=context)


#gobal subject 
def global_subject(request,subject_id=None):
     # get the subject by id 
    sub_subjects=None
    subject_get=Subject.objects.get(pk=subject_id)  
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    #get the subject content and parse it to html
    soup=BeautifulSoup(subject_get.subject_contnet,"html.parser")
    #change all img src in the subject content to url  by replace the id number of image by url
    for img in soup.find_all("img"):
        print(subject_get.subject_image_set.get(id=int(img['src']) ).image.url )
        img_url=subject_get.subject_image_set.get(id=int(img['src']) ).image.url 
        img['src']=img_url 
    context={
        "object":subject_get,
        "content":str(soup),
        "sub_subjects":sub_subjects
    }
   
    return render(request,"htmlFiles/subjects.html",context=context)



def reports(request,page):

    
    paginator=Paginator(report.objects.all(),5)
    
    reports=paginator.get_page(page)
    
    #reports=paginator.get_elided_page_range(number=page)
   

    
    context={
        "reports":reports,
        "page_number":paginator.get_elided_page_range(number=page,on_each_side=1,on_ends=1),#range(1,reports.paginator.num_pages+1),
        "next":reports.number+1,
        "previous":reports.number-1,
        "paginator":paginator,
        
    }

    return render(request,"htmlFiles/reports.html",context=context)


def report_page(request,report_id=None):

    try:
        report_obj=report.objects.get(id=report_id)
    except report.DoesNotExist:
        raise Http404

    return render(request,"htmlfiles/report.html",{"report":report_obj})




def handling_404(request,exception):

    return render(request,"htmlFiles/handlers/handle_404.html")




def search(request):

    if request.method == 'GET':
        search_data=request.GET["search"]
        result_subject=Subject.objects.filter(title__icontains=search_data)
        result_report=report.objects.filter(title__icontains=search_data)
        result=chain(result_subject,result_report)
        print(result)
        #print(result[0].sub_subjects_set.all()[0].main_title_en())
    else:
        result="False"

    return render(request,"htmlFiles/search.html",{"result":result})




def subject_set_parent(request,subject_id=None):
     # get the subject by id 
   
    subject_geted=Subject.objects.get(pk=subject_id)
    #subject without parent
    free_subjects=[]
    all_subjects=Subject.objects.all()

    for subject in all_subjects:
        if subject.sub_subjects == None and subject.main_title == None:
            free_subjects.append(subject)
        
 
    if request.method=="POST":
        post_data=request.POST.getlist("free_subjects")
        print(post_data)
        #convert post_data id from string to int
        int_list = [int(s) for s in post_data]

        obj_by_id=Subject.objects.filter(id__in=int_list)
        for obj in obj_by_id:
            obj.sub_subjects=subject_geted
            obj.save()

        print(obj_by_id)
    

    return render(request,"htmlFiles/admin/subject_set_parent.html",{"subject":subject_geted,"free_subjects":free_subjects})




def subject_parent_remove(request,subject_id=None):
     # get the subject by id 
    subject_geted=Subject.objects.get(pk=subject_id)

    all_children=subject_geted.subject_set.all() 
 
    if request.method=="POST":
        post_data=request.POST.getlist("free_subjects")
        print(post_data)
        #convert post_data id from string to int
        int_list = [int(s) for s in post_data]

        obj_by_id=Subject.objects.filter(id__in=int_list)
        for obj in obj_by_id:
            obj.sub_subjects=None
            obj.save()
            
        print(obj_by_id)
    

    return render(request,"htmlFiles/admin/subject_parent_remove.html",{"subject":subject_geted,"all_children":all_children})


def subject_list(request):

    all_subjects=Subject.objects.all()

    return render(request,"htmlFiles/admin/subject_list.html",context={"subjects":all_subjects})\
    






def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)

        if form.is_valid():

            user=form.save()
            profile=Profile.objects.create(user=user)
            profile.save()
            login(request,user)

            return redirect("main")
    
    else:
        form=SignUpForm()
    
    return render(request,"htmlFiles/signup.html",{"form":form})



@login_required
def profile(request):

    if request.method=="POST":
        if "img" in request.POST:
            data=request.FILES["profile_image"]
            profile=request.user.profile
            profile.image=data
            profile.save()

        if "first_name" in request.POST:
            data=request.POST["firstname"]
            """  if User.objects.filter(username=data).exists():
                raise ValidationError('This username already exists')
            else: """

            request.user.first_name=data
            request.user.save()

        if "last_name" in request.POST:
            data=request.POST["lastname"]
            """  if User.objects.filter(username=data).exists():
                raise ValidationError('This username already exists')
            else: """

            request.user.last_name=data
            request.user.save()

        if "phone" in request.POST:

            data=request.POST["phone_number"]

            profile=request.user.profile
            profile.phone_number=data
            profile.save()

        if "birth_date" in request.POST:

            data=request.POST["birth"]

            profile=request.user.profile
            profile.birthdate=data
            profile.save()



       
    else:
        return render(request,"htmlFiles/profile.html")
    return render(request,"htmlFiles/profile.html")





def edit_subject(request,subject_id=None):


    return render(request,'htmlFiles/edit_subject.html',context={"test":"test"})