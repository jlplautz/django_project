# django_project

Python Django Tutorial: Full-Featured Web App from Corey Schafer

![Python aplication](https://github.com/jlplautz/django_project/workflows/Python%20aplication/badge.svg)
[![Updates](https://pyup.io/repos/github/jlplautz/django_project/shield.svg)](https://pyup.io/repos/github/jlplautz/django_project/)
[![Python 3](https://pyup.io/repos/github/jlplautz/django_project/python-3-shield.svg)](https://pyup.io/repos/github/jlplautz/django_project/)

# Criado o diretório django_project
- pipenv shell
- (django_project) django_project $pipenv install django
- (django_project) django_project $pipenv install flake8
- (django_project) django_project $ pip freeze > requirements.txt
- (django_project) django_project $ tree
```
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
└── README.md
```
- (django_project) django_project $ pip freeze > requirements.txt

- create file -> .flake8
```
[flake8]
max-line-length = 120
exclude = .venv
```

- create a file .pyup.yml
```
requirements:
  - Pipfile
  - Pipfile.lock
```
- (django_project) django_project $ python -m django --version
> 3.0.6

<h5> When we use (.) to creat a django project - the project is going to be create in the same directory</h5>

- (django_project) django_project $ django-admin startproject djangoproject .
```
(django_project) django_project $ tree
.
├── djangoproject
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── LICENSE
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt

```

- (django_project) django_project $ mng runserver

# Create a new app in the djangoproject
- (django_project) django_project $ mng startapp blog
```
(django_project) django_project $ tree
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── djangoproject
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── LICENSE
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt
```

# in the file blog/views.py
```
from django.http import HttpResponse
def home(request):
    return HttpResponse(<h1>Blog Home</h1>)

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

<h5>Create a file blog/urls.py and copy from djangoproject/urls.py</h5>
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
```

<h5>insert in the file djangoproject/urls.py</h5>
```
from django.urls import path, include  <- we inserted include
urlpatterns = [
    path('admin/', admin.site.urls),
    # when we leave the path ('', ...) then we can access it directly
    path('', include('blog.urls')), <- we insert this line
]
```

<h5>Create a blog/templates/blog</h5>

- blog $ mkdir templates/
- blog $ mkdir templates/blog <- is is django convention
  > ex: blog -> templates -> blog -> template.html

<h5>Create inside of blog/templates/blog two files:</h5>
- created via pycharm -> home.html
- created via pycharm -> about.html
```
templates $ tree
.
└── blog
    ├── about.html
    └── home.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Bloag Home!</h1>
</body>
</html>
```

- in the file apps.py -> verify the class BlogConfig
```
class BlogConfig(AppConfig):
    name = 'blog'
```

- in the setting.py file insert in the INSTALLED_APPS
````
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    ...
]
````
- in the views.py file we need to modify
```
def home(request):
    # from views -> is routing a response to user
    # return HttpResponse('<h1>Blog Home</h1>')

    # from views -> is routing to a tempĺate
    return render(request, 'blog/home.html')
```

- create a dummy date in the file views
```
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
```

- modify the function home:
```
    # context to receive de posts (dummy data) 
    context = {
        'posts': posts
    }
    # from views -> is routing to a tempĺate, with contecxt information
    return render(request, 'blog/home.html', context)
```

- modify the templates ->  home.html
```
<body>
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
            <p>By {{ post.author }} on {{ post.date_posted }}</p>
            <p>{{ post.content }}</p>
    {% endfor %}
</body>
```

- there is a modification in the head tag ->  home.html
```
# just to verify the title of the page 
    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
```