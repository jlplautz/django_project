from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


def home(request):
    # from views -> is routing a response to user
    # return HttpResponse('<h1>Blog Home</h1>')

    # context to receive de posts (dummy data)
    context = {'posts': Post.objects.all()}
    # from views -> is routing to a tempĺate, with context information
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
