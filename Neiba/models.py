from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def save_loc(self):
        self.save()

    def __str__(self):
        return self.name
    
class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to = 'media/', null = True, blank = True)
    about = models.TextField(max_length=200, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cop_dail = models.IntegerField(null=True, blank=True)
    health_dail = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name