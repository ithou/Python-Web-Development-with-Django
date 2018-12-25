from django.shortcuts import render
from .models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/archive.html', context)

