from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm
# Create your views here.

def welcome(request):
    all_images = Image.get_all_images()
    insta_users = Profile.get_all_instagram_users()
    return render(request, 'welcome.html', {"all_images":all_images, "insta_users":insta_users})

# @login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')

    else:
        form = NewProfileForm()
    return render(request, 'welcome.html', {"form": form})