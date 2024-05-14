from django.contrib import admin
from django.db import models
from django import forms
from .models import Subject,subject_image,report,Profile,Mail,Doctor
from django.utils.html import format_html
from django.urls import reverse_lazy
from django.forms import Textarea

# Register your models here.


class IngredientInline1(admin.TabularInline):
    model = subject_image
    fields=['pk','image','copy_button']
    readonly_fields=['pk','copy_button']
    extra=1

    class Meta:
        js='js/admin_config.js'


    def copy_button(self,obj):
        return format_html("<input type='text' value='<img src={data} />'  />",data=obj.id)

    


@admin.register(Subject)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title','main_title','id',"get_parent")
    search_fields = ('title', )
    formfield_overrides = {
        models.ManyToManyField: {
            "widget": forms.CheckboxSelectMultiple,
        },
        models.TextField:{
                "widget": Textarea(
                    attrs={
                        'rows':50,
                        'cols':100,
                    }
                )
        }
    }
    inlines = [IngredientInline1,]

    """  def edit(self,obj):
        return format_html('<a href="{url}">edit</a>',url=reverse_lazy('edit_subject',kwargs={'subject_id':obj.id}))
    """
    def get_parent(self,obj):

        if obj.sub_subjects is not None:
            return obj.sub_subjects.title
        else:
            return "free"
    get_parent.short_description = 'get_parent'

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display=("user",'subject','email_reply','replied','user_visible','created')

@admin.register(subject_image)
class MailAdmin(admin.ModelAdmin):
    list_display=("id","subject")

admin.site.register(report)
admin.site.register(Profile)
admin.site.register(Doctor)