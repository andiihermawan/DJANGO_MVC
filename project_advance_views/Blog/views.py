from django.shortcuts import render
from .models import Blog
# Create your views here.
def BlogPost(request):
    blog = Blog.objects.all()
    return render(request, 'Blog/blog.html',{'blog':blog})
