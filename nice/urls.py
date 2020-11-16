from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('category/',views.search_results,name='category'),
    path('location',views.location,name='location'),
    # re_path('search', views.search_image, name='search_results'),
    
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)