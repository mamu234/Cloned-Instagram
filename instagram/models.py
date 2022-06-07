
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField(upload_to='postImages',blank=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title
class Tag(models.Model):
    name=models.CharField(max_length=300, blank=True)
    description=models.TextField(blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Image file',upload_to = 'blogs/images/', null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    bio = models.CharField(max_length = 255)
    # date_joined = models.DateTimeField(default=datetime.timezone.now)

    def __str__(self):
        return self.user

class Comment(models.Model):
    post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length = 255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent=comment=models.ForeignKey('self',on_delete=models.CASCADE)
    datatime=models.DateTimeField(default=now)

    def __str__(self):
        return self.post
    
    class Meta:
     abstract = True

class Following(models.Model):
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)


    def __str__(self):
        return self.username

