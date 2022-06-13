from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('',views.home, name='index'),
    path('registration/',views.register, name='registration'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
]

