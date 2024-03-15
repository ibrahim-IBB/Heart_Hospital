from django.contrib import admin
from django.db import models
from django import forms
from .models import Subject,subject_image,report

# Register your models here.


class IngredientInline1(admin.TabularInline):
    model = subject_image
    


@admin.register(Subject)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title','main_title','id')
    search_fields = ('title', )
    formfield_overrides = {
        models.ManyToManyField: {
            "widget": forms.CheckboxSelectMultiple,
        },
    }
    inlines = [IngredientInline1]

admin.site.register(report)


