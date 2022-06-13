from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.
from .models import Post ,Profile,photos

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(photos)
