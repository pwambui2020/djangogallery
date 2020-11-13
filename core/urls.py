from django.conf.urls import url
from . import views
# from . import images

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]