from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def category(request):
    
    return render(request, 'all-nice/category.html')
def location(request):
    return render(request, 'all-nice/location.html')