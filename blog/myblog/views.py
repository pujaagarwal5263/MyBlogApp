from django.shortcuts import render
from .models import Blogpost
from django.conf import settings
# Create your views here.
def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'myblog/index.html', {'myposts': myposts})
def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'myblog/blogpost.html',
                  {'post':post})