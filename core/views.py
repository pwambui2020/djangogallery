from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Posh Gallery')