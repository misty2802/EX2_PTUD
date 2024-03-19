from django.contrib import admin
from .models import CV

@admin.register(CV)
class CVModelAdmin(admin.ModelAdmin):
    list_display=['id', 'profile_image', 'name','phone','email','linkedin_link','locality','education','language','profile','experience','profession_skills','interests']
# Register your models here.
