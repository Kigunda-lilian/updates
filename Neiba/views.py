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
    return render(request, "user/profile.html", {"profile": profile, 'hood': hood, 'businesses': businesses, "posts": posts, })


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

    return render(request, 'user/profile_update.html', {"form": form})

@login_required(login_url="/users/login/")
def all_profile(request):
    current_user = request.user
    accounts = Profile.objects.all().order_by('-user')
    return render(request, 'user/all_profile.html', {'accounts': accounts, 'current_user': current_user})

@login_required(login_url="/users/login/")
def create_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = NeighbourhoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/neighbourhood')
    else:
        hood_form = NeighbourhoodForm()
    context = {'hood_form': hood_form}
    return render(request, 'main/create_hood.html', context)

@login_required(login_url="/users/login/")
def neighbourhood(request):
    current_user = request.user
    hood = Neighbourhood.objects.all().order_by('-id')
    return render(request, 'main/neighbourhood.html', {'hood': hood, 'current_user': current_user})

@login_required(login_url='/users/login/')
def one_hood(request, name):
    current_user = request.user
    hood = Neighbourhood.objects.get(name=name)
    profiles = Profile.objects.filter(hood=hood)
    busineses = Business.objects.filter(hood=hood)
    posts = Post.objects.filter(name=name)
    request.user.profile.hood = hood
    request.user.profile.save()

    return render(request, 'main/one_hood.html', {'hood': hood, 'busineses': busineses, 'posts': posts, 'current_user': current_user, 'profiles': profiles})

def join_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)

    request.user.profile.hood = hood
    request.user.profile.save()
    return redirect('neighbourhood')


def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('neighbourhood')

@login_required(login_url='/users/login/')
def create_business(request):
    current_user = request.user
    if request.method == "POST":

        form = BusinessForm(request.POST, request.FILES)

        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.name = request.POST['name']
            business.save()
        return HttpResponseRedirect('/busineses')
    else:
        form = BusinessForm()
    return render(request, 'main/create_business.html', {'form': form, 'profile': profile})

@login_required(login_url="/users/login/")
def busineses(request):
    current_user = request.user
    busineses = Business.objects.all().order_by('-id')

    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()

        locations = Location.objects.all()
        hood = Neighbourhood.objects.all()

        busineses = Business.objects.all().order_by('-id')

        return render(request, "user/profile.html", {"danger": "Update Profile", "locations": locations, "hood": hood, "busineses": busineses})
    else:
        hood = profile.hood
        busineses = Business.objects.all().order_by('-id')
        return render(request, "main/bizna.html", {"busineses": busineses})

@login_required(login_url="/users/login/")
def create_post(request):
    current_user = request.user.id
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            location = Profile.objects.get(user_id=current_user)
            post.user = current_user
            post.save()

        return HttpResponseRedirect('/post')
    else:
        form = PostForm()
    return render(request, "main/create_post.html", {'form': form})


login_required(login_url="/users/login/")
def post(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    post = Post.objects.all().order_by('-name')
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        post = Post.objects.all().order_by('-name')

        location = Location.objects.all()
        hood = Neighbourhood.objects.all()

        busineses = Business.objects.filter(user_id=current_user.id)

        return render(request, "user/profile.html", {"danger": "Update Profile ", "location": location, "hood": hood,  "busineses": busineses, "post": post})
    else:
        hood = profile.hood
        post = Post.objects.all().order_by('-name')
        return render(request, "main/post.html", {"post": post})
