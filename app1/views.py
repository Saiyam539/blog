from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    blogs = Blogs.objects.all()
    
    context = {
        'blogs':blogs
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def post(request):
    return render(request,'post.html')


def view_post(request,id):
    blog_post = Blogs.objects.get(id=id)
    
    context = {
        'blog':blog_post
    }
    return render(request,'post.html',context)