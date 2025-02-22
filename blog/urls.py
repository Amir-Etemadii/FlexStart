from django.urls import path
from . import views

app_name= 'blog'

urlpatterns= [
    path('blogs', views.blog, name='blogs'),
    path('post-category/<str:category_name>', views.post_category, name='post-category'),
]