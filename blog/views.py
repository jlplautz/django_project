from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

def home(request):
    # from views -> is routing a response to user
    # return HttpResponse('<h1>Blog Home</h1>')

    # from views -> is routing to a tempĺate
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
