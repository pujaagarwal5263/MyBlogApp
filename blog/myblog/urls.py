from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index),
    path('blogpost/<int:id>', views.blogpost, name="blogPost"),
]