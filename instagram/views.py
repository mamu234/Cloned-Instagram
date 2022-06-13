from django.shortcuts import render
from .models import Post
# Create your views here.
from .models import photos


def home(request):
    posts =Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})
