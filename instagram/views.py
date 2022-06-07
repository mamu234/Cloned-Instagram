from django.shortcuts import render,redirect
from django.http  import HttpRequest, HttpResponse
from .models import Post
from .forms import PostCreate




def welcome(request):
    posts=Post.objects.all()
    return render(request, 'welcome.html',{'posts':posts})
def upload(request):
    if request.Method== 'POST':
        upload=PostCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('welcome')

        else:
         return HttpResponse('your form is not valid')
    else:
        return render(request,'upload_form.html',{'upload':upload})

def update_post(request,post_id):
    post_id=int(post_id)
    try:
     post_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('welcome')
    post_form=PostCreate(request.POST or None,instance=post_up)
    if post_form.is_valid():
        post_form.save()
        return redirect('welcome')
    return render(request,'upload_form.html',{'upload':post_up})

def delete_post(request, post_id):
    try:
        post_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('welcome')
    post_up.delete()
    return redirect('welcome')
    



def profile(request):
    return render(request, 'profile.html')



