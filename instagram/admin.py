from django.contrib import admin

from instagram.models import Following, Post, Profile, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Following)
admin.site.register(Tag)

