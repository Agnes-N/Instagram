from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    all_images = Image.get_all_images()
    insta_users = Profile.get_all_instagram_users()
    return render(request, 'welcome.html', {"all_images":all_images, "insta_users":insta_users})

