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

@login_required(login_url="/users/login/")
def search(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        hoods_searched = Neighbourhood.objects.filter(
            name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "users/search.html", {"message": message, "neighbourhood": hoods_searched})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})
    
@login_required(login_url="/users/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    hood = Neighbourhood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    posts = Post.objects.filter(user_id=current_user.id)
    return render(request, "all-temps/profile.html", {"profile": profile, 'hood': hood, 'businesses': businesses, "posts": posts, })


@login_required(login_url="/users/login/")
def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    return render(request, 'user/update_prof.html', {"form": form})