from django import forms
from .models import *
from django.forms import ModelForm
from django.db.models import fields

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']