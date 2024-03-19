
from django.db import models
from django.contrib.auth.models import AbstractUser


class CV(models.Model):
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    name =models.CharField(max_length=100,blank=False, null=False)
    position= models.CharField(max_length=100,blank=False, null=False)
    phone = models.CharField(max_length =20, blank=False, null=False)
    email = models.EmailField(max_length = 255)
    linkedin_link = models.URLField(blank=True, null=True)
    locality =models.CharField(max_length =255, blank=True, null=True)
    education = models.TextField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    profession_skills = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)