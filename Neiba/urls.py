"""Habari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('users/profile/', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.all_profile, name='profiles'),
    path('search/', views.search, name='search'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('create_neighbourhood', views.create_neighbourhood,
         name='create_neighbourhood'),
    path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
    path('hood/<str:name>', views.one_hood, name='single_hood'),
    path('join_hood/<int:id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:id>', views.leave_hood, name='leave_hood'),
    path('create_business', views.create_business, name='create_business'),
    path('busineses/', views.busineses, name='busineses'),
    path('create_post', views.create_post, name='create_post'),
    path('post/', views.post, name='post'),
  
]

