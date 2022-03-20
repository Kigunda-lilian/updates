from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Coding Business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    