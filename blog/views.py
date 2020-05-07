from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        "title": 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 06, 2020'
    },
    {
        'author': 'Jane Doe',
        "title": 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 07, 2020'
    }
]

# Create your views here.


def home(request):
    # from views -> is routing a response to user
    # return HttpResponse('<h1>Blog Home</h1>')

    # context to receive de posts (dummy data)
    context = {
        'posts': posts
    }
    # from views -> is routing to a tempĺate, with contecxt information
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
