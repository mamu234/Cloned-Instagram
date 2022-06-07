from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('upload/', views.upload, name='upload'),
    path('update_post/<int:post_id>', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]