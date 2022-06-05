from django.contrib import admin

from instagram.models import Following, Post, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Following)