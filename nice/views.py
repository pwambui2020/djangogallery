
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Images, Location, Category

# Create your views here.
def welcome(request):
    images = Images.objects.all()
    locations = Location.objects.all()
    return render(request,'welcome.html',{'images':images,'locations':locations})

def category(request):
    images=Images.objects.all()
    return render(request, 'all-nice/category.html', {'images':images})

def location(request):
    return render(request, 'all-nice/location.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_category = Images.search_by_category(category)
        message = f"{category}"

        return render(request, 'all-nice/search.html',{"message":message,"images": searched_category,"category":category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-nice/search.html',{"message":message})    
    
