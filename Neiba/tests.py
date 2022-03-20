from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Coding Business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business.save()
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)
        
        
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Moringa School')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    