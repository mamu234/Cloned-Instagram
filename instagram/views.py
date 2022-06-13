from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
from .models import photos
from django.contrib import messages
from .forms import UserRegisterForm


def home(request):
    posts =Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Your account has been created! You are now able to log in') # Show sucess message when account is created
            return redirect('login') # Redirect user to Login page
    else:
        form = UserRegisterForm()
    return render(request,'registration/registration.html', {'form': form})