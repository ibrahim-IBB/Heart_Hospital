from django.shortcuts import render
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.http import Http404
from itertools import chain
# Create your views here.
from .models import Subject
from .models import report




def contact_info(request):

    return render(request,"htmlFiles/contact_info.html")

def main(request):

    recent_reports=report.objects.order_by('-created')[1:9]
   
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
        print("there is no id")

        subject_get=Subject.objects.get(main_title="حول المستشفى")
    else:
        print("id founded")
        subject_get=Subject.objects.get(pk=subject_id)
        print(subject_get)

    print("#$$$$$$$$$$$$$$$$$$$$")
    
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    print("#$$$$$$$$$$$$$$$$$$$$")
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

    print("#$$$$$$$$$$$$$$$$$$$$")
    
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    print("#$$$$$$$$$$$$$$$$$$$$")
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

    print("#$$$$$$$$$$$$$$$$$$$$")
    
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    print("#$$$$$$$$$$$$$$$$$$$$")
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
   
    print("id founded")
    subject_get=Subject.objects.get(pk=subject_id)
    print(subject_get)

    print("#$$$$$$$$$$$$$$$$$$$$")
    
    #get all sub subjects 
    sub_subjects=subject_get.subject_set.all()
    print("#$$$$$$$$$$$$$$$$$$$$")
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
   
    return render(request,"htmlFiles/subjects.html",context=context)



def reports(request,page):

    
    paginator=Paginator(report.objects.all(),2)
    
    reports=paginator.get_page(page)



    
    context={
        "reports":reports,
        "page_number":range(1,reports.paginator.num_pages+1),
        "next":reports.number+1,
        "previous":reports.number-1
        
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
    print("#$$$$$$$$$$$$$$$$$$$$")

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
    print("#$$$$$$$$$$$$$$$$$$$$")

    return render(request,"htmlFiles/admin/subject_parent_remove.html",{"subject":subject_geted,"all_children":all_children})


def subject_list(request):

    all_subjects=Subject.objects.all()

    return render(request,"htmlFiles/admin/subject_list.html",context={"subjects":all_subjects})