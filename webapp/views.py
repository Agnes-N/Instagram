from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm,NewImageForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    all_images = Image.get_all_images()
    insta_users = Profile.get_all_instagram_users()
    current_user = request.user
    myprof = Profile.objects.filter(id = current_user.id).first()
    return render(request, 'welcome.html', {"all_images":all_images, "insta_users":insta_users, "myprof":myprof})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

   
@login_required(login_url='/accounts/login/')
def my_profile(request):

    current_user = request.user
    profi_images = Image.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"profi_images":profi_images, "my_profile":my_profile})


@login_required(login_url='/accounts/login/')
def new_image(request):

    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'upload.html', {"form": form})
