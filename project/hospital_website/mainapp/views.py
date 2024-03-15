from django.shortcuts import render
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
from .models import Subject
from .models import report




def contact_info(request):

    return render(request,"htmlFiles/contact_info.html")

def main(request):

    recent_reports=report.objects.order_by('-created')[1:5]
   
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
    sub_subjects=subject_get.sub_subjects.all()
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
    sub_subjects=subject_get.sub_subjects.all()
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
    sub_subjects=subject_get.sub_subjects.all()
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
        result=Subject.objects.filter(title__icontains=search_data)
        #print(result[0].sub_subjects_set.all()[0].main_title_en())
    else:
        result="False"

    return render(request,"htmlFiles/search.html",{"result":result})