from django.contrib import admin
from django.db import models
from django import forms
from .models import Subject,subject_image,report,Profile

# Register your models here.


class IngredientInline1(admin.TabularInline):
    model = subject_image
    


@admin.register(Subject)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title','main_title','id',"get_parent")
    search_fields = ('title', )
    formfield_overrides = {
        models.ManyToManyField: {
            "widget": forms.CheckboxSelectMultiple,
        },
    }
    inlines = [IngredientInline1]

    def get_parent(self,obj):

        if obj.sub_subjects is not None:
            return obj.sub_subjects.title
        else:
            return "free"
    get_parent.short_description = 'get_parent'

admin.site.register(report)
admin.site.register(Profile)

