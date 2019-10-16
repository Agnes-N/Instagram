from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image
# Create your views here.

def welcome(request):
    all_images = Image.get_all_images()
    return render(request, 'welcome.html', {"all_images":all_images})