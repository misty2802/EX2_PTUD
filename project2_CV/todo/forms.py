from django import forms
from .models import CV  

class CVform (forms.ModelForm):
    class Meta:
        model =CV 
        fields =['profile_image', 'name','position','phone','email','linkedin_link','locality','education','language','profile','experience','profession_skills','interests']
        
        labels = {'profile_image':'Profile Image', 'name':'Full Name','position':'Position','phone': 'Mobile No','email':'Email ID','linkedin_link':'Linkedin','locality':'Address','education':'Education','language': 'Language','profile':'Profile','experience':'Experience','profession_skills':'Profession Skills','interests':'Interests'}
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin_link':forms.TextInput(attrs={'class': 'form-control'}),
            'locality':forms.TextInput(attrs={'class': 'form-control'}),
            'education':forms.TextInput(attrs={'class': 'form-control'}),
            'language':forms.TextInput(attrs={'class': 'form-control'}),
            'profile':forms.TextInput(attrs={'class': 'form-control'}),
            'experience':forms.TextInput(attrs={'class': 'form-control'}),
            'profession_skills':forms.TextInput(attrs={'class': 'form-control'}),
            'interests':forms.TextInput(attrs={'class': 'form-control'}),
        }