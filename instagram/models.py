from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.

from django.db import models
from django.utils import timezone # Import timezone for DateTimeField
from django.contrib.auth.models import User # Import User model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If a user created the post is deleted, posts are deleted as well.ß

    # __str__() method returns how the Post is printed
    def __str__(self):
        return self.title


# class Tag(models.Model):    
#     name =models.CharField(max_length=100,blank=True)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return f'{self.name} Tag'

# # class Post(models.Model):
# #     title = models.CharField(max_length=300)
# #     author = models.ForeignKey(User,on_delete=models.CASCADE)
# #     content = models.TextField()
# #     image = models.ImageField(upload_to='blogs/blogImages',blank=True)
# #     dateTime = models.DateTimeField(auto_now_add=True)
# #     slug = models.SlugField(max_length=100)
# #     tags = models.ManyToManyField(Tag)
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE) 

   
#     def __str__(self):
#         return self.title


#     def __str__(self):
#         return f'{self.title} BlogPost'

# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     image = models.ImageField('Image file', upload_to='blogs/profile',null=True)
#     first_name = models.CharField(max_length=30, null=True)
#     last_name = models.CharField(max_length=30, null=True)
#     bio = models.TextField(max_length=255, null=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     @receiver(post_save, sender=User)
#     def create_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
    
#     @receiver(post_save, sender=User)
#     def save_profile(sender, instance, **kwargs):
#         instance.profile.save()



#     def __str__(self):
#         return f'{self.user} Profile'

# class Comment(models.Model):
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     blog = models.ForeignKey(Post,on_delete=models.CASCADE)
#     parent_comment = models.ForeignKey('self',on_delete=models.CASCADE)
#     dateTime = models.DateTimeField(default=timezone.now)


#     def __str__(self):
#         return f'{self.content} Comment'