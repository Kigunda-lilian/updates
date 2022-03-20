from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save


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
    
    def create_hood(self):
        self.save()

    @classmethod
    def delete_hood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    @classmethod
    def find_hood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    @classmethod
    def update_hood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def update_occupants(cls, occupants_count):
        cls.objects.filter(occupants_count=occupants_count).update()
        
class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', null=True)
    photo = models.ImageField(upload_to = 'media/', null = True, blank = True)
    bio = models.TextField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL,
                             null=True, related_name='members', blank=True)
    contact = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
class Business(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    about = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def create_business(self):
        self.save()

    def update_business(self):
        self.update()

    def delete_business(self):
        self.delete()
        
    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def find_business(cls, id):
        business = cls.objects.get(id=id)
        return business

    def __str__(self):
        return self.name
    
class Post(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=800, blank=True, null=True)
    photo = models.ImageField(upload_to = 'media/', null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def create_post(self):
            self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()
        
    @classmethod
    def search_by_name(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def find_post(cls, id):
        post = cls.objects.get(id=id)
        return post

    class Meta:
        ordering = ['-date_created']

    def _str_(self):
        return self.name
    
