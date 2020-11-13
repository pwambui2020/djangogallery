from django.shortcuts import render
from dashboard.models import Order

# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Posh Gallery')

def search_results(request):
    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})