from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    #path, name of function, namespace 
    path('', views.home, name='home'),
]