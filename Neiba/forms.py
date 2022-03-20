from django import forms
from .models import *
from django.forms import ModelForm
from django.db.models import fields

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio', 'contact', 'location', 'hood']
        
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'photo', 'about',
                  'location', 'cop_dail', 'health_dail']
        
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email', 'about', 'location', 'hood']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'location')

