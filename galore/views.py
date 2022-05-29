from django.shortcuts import render
from django.http import Http404
from .models import Image,Category


# Create your views here.
def gallery(request):
    return render(request, 'gallery.html')

def display_image(request):
    category = Category.objects.all()
    image = Image.objects.all()
    return render(request,'all-images.html',{'image':image,'category':category})