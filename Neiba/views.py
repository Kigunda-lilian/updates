from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='/users/login/')
def index(request):
    hood = Neighbourhood.objects.all().order_by('-name')
    return render(request, 'main/index.html')

