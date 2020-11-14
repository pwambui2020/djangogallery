from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('category',views.category,name='category'),
    path('location',views.location,name='location')
    
]