from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Diseases)
class DiseaseAdmin(admin.ModelAdmin):
    list_display =['id','age', 'sex', 'cp', 'trestbps', 'chol',
       'fbs', 'restecg', 'max_heart_rate',
       'exercise_angina', 'oldpeak', 'slope', 'target']

@admin.register(Doctors)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' ,'image' , 'spciality' ,'address','contact','desc']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' ,'image' , 'publish_by' ,'desc']



admin.site.site_header = 'CARDIOLOGY CARE'
admin.site.unregister(Group)