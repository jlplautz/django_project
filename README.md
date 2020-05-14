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

<h4> Insert into blog/views.py</h4>

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

<h5>Insert in the file djangoproject/urls.py</h5>
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

<h5> TEMPLATE INHERITANCE </h5>

- create a new templates/blog/base.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```
- template inheritance -> modify templates/blog/home.html
```
{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
        <h1>{{ post.title }}</h1>
        <p>By {{ post.author }} on {{ post.date_posted }}</p>
        <p></p>{{ post.content }}</p>
    {% endfor %}
{% endblock content %}
```
- template inheritance -> modify templates/blog/about.html
```
{% extends "blog/base.html" %}
{% block content %}
    <h1>About Page!</h1>
{% endblock content %}
```

<h5> BOOTSTRAP - Popular library</h5>

- https://getbootstrap.com/ -> Starter template
- copied from bootstrap - starter temnplate
- base.html
    - we copy links to insert in the head tag 
    - and script to insert into the body tag
    - insert div tag ...
- the code was copied from github
https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog/03-Templates/django_project/blog 

<h5>Directory static/blog was creaed and a file main.ccs</h5>

- file main.css was copied from -> ttps://github.com/CoreyMSchafer/code_snippets/...

<h5>Two additional lines was implemented in the file base.html</h5>

- {% load static %}
- head tag -> <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

<h5>Important information to insert into the navbar</h5>

- we can insert the url path by the url name.
  - <a class="nav-item nav-link" href="/">Home</a> <- old 
  - <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a> <- name 'blog-home' <- defined in urls.py file
  - <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a> <- name 'blog-about'
  
<h5>django-admin page</h5>

- (django_project) django_project $ mng makemigration
- (django_project) django_project $ mng migrate
- (django_project) django_project $ mng createsuperuser

```
(django_project) django_project $ mng makemigrations
No changes detected

(django_project) django_project $ mng migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK

(django_project) django_project $ mng createsuperuser
Username (leave blank to use 'plautz'): admin
Email address: admin@admin.com
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

<h3>Database connection - SQlite</h3>

- file blog/models.py

```
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posed = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

- by command -> mng sqlmigarte blog 0001 -> we can see the SQL command:
```
(django_project) django_project $ mng sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                          "title" varchar(100) NOT NULL, 
                          "content" text NOT NULL, 
                          "date_posed" datetime NOT NULL, 
                          "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```
- command mng migrate
```
(django_project) django_project $ mng migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

<h3>Using command via terminal => mng shell</h3>

- (django_project) django_project $ mng shell
    - from blog.models import Post 
    - from django.contrib.auth.models import User
    - User.objects.all()
        - <QuerySet [<User: admin>]>
    - User.objects.first()
        - <User: admin>
    - User.objects.filter(username='admin')
        - <QuerySet [<User: admin>]>
    - user = User.objects.filter(username='admin').first()
    - user
        - <User: admin>
    - user.id
        - 1
    - user.pk
        - 1
    - user = User.objects.get(id=1)
    - user
        - <User: admin>
    - Post.objects.all()
        - <QuerySet []>
    - post_1 = Post(title='Blog 1', content='First post Content!', author=user)
    - post_1.save()
    - Post.objects.all()
        - <QuerySet [<Post: Post object (1)>]>
    - a function was implemented in the blog/models.py def __str__(self)
    
    - Post.objects.all()
        - <QuerySet [<Post: Blog 1>]>
 
    - post_2 = Post(title='Blog 2', content='Second Post Content!', author_id=user.id)
    - post_2.save()
    - Post.objects.all()
        - <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
    - post = Post.objects.first()
    - post.id
        -1
    - post.content
        -'First post Content!'
    - post.date_error_message(  post.date_posed           
    - post.date_posed
        - datetime.datetime(2020, 5, 8, 21, 7, 11, 180104, tzinfo=<UTC>)
    - post.author
        - <User: admin>
    - post.author.email
        - 'jorge.plautz@gmail.com'
    - user.post_set
        - <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7f88a6dab520>
    - user.post_set.all()
        - <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
    
    - user.post_set.create(title='Blog 3', content='Third Post Content!')
        - <Post: Blog 3>
    - ( observe that we don't need to save() the last create blog))
    - Post.objects.all()
        - <QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>

<h2> Web App Part 5 - Database and Migrations </h2> 

<h3>Delete de dummy data from blog/views.py</h3 >

- in the function home, we need to modify the request information to the context
    - context = {'posts': Post.objects.all()}
    
- Procedure to modify the date apresentation in the template
    - <small class="text-muted">{{ post.date_posed }}</small>
    - <small class="text-muted">{{ post.date_posed | date:"F d, Y" }}</small>
    
<h5>To access the new database table from django-admin</h5>
- insert into file blog/admin.py

```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

<h2> Web App Part 6 - User Registration </h2>
<h3>Create a user registration page- to loging account</h3>
<h3>learning how we can use Form - to create user </h3 >

- create a new app inside of the project
    - (django_project) django_project $ mng startapp users
    
```
(django_project) django_project $ tree -d
.
├── blog
│   ├── migrations
│   │   └── __pycache__
│   ├── __pycache__
│   ├── static
│   │   └── blog
│   └── templates
│       └── blog
├── djangoproject
│   └── __pycache__
└── usersf
    └── migrations
```

- setting.py file insert -> INSTALLED_APPS
    - 'users.apps.UsersConfig',

- Configure the views.py file in the users app

```textmate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```

- create in the users app a templates/users/register.html

```
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
{#      CSRF - cross-site request forgery token and this will protect our form against certain attacks#}
{#             just some added security that Django requires#}
        <form method="POST">
            {% csrf_token %}  
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Join Today</legend>
                {{ form }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Sign Up</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Already have an account? <a class="ml-2" href="#">Sing In</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

- need to create a URL pattern - in urls.py file
- we can use the view directly by importing it from users
```
from users import views as user_views

urlpatterns = [
    ...
    path('register/', user_views.register, name='register'),
]
```

- To save the information collected in the template register.html
    - modify the users/views.py

```
from django.shortcuts import render, redirect

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```

- the page is going to be redirect to blog-home, 
  the we need to prepare the base.html templates to show the alarm
  We are going to shoe the message in the main container
```
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
{% block content %}{% endblock %}
```

- to save the new created user in the users/views.py
    - form.save()
    
- create a new form - it is going to be a new file users/forms.py
  And it is going to create our first form that inherits from the user creation form.
  
```
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

- modify the users/views.py file
```
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
```

- Just to get a better template/users/register apresentation by crispy forms
    - (django_project) django_project $ pipenv install django-crispy-forms

- in the setting.py file inserted it into INSTALLED_APPS
    - 'crispy_forms',
    - CRISPY_TEMPLATE_PACK = 'bootstrap4' <- insert it in the end of setting.py file

- in the file register.html insert
    - {% load crispy_forms_tags %}
    - {{ form|crispy }}

<h2> Web App Part 7 -  Login and Logout System </h2> 
<h3> learning how to create an authentication system for Django App</h3 >
    
- Project URLs module - urls.py module
    - these are class-based views
    
```
from django.contrib.auth import views as auth_views  # auth_views for django.contrib.auth

urlpatterns = [
    ...
    path('login/', auth_views.LoginView.as_views(), name='loging'),
    path('logout/',auth_views.LogoutView.as_views(),name='logout'),
    ...
]
```

- in the urlpatterns we can tell Django where to look for a template, 
  as one argument as ViewFunction 
  
```
from django.contrib.auth import views as auth_views  # auth_views for django.contrib.auth

urlpatterns = [
    ...
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='loging'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    ...
]
```

- created a file users/templates/users/login.html
```
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
{#      CSRF - cross-site request forgery token and this will protect our form against certain attacks#}
{#             just some added security that Django requires#}
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Log In</legend>
{#                to render or form in paragraph tags insert -> for.as_p#}
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Need an account? <a class="ml-2" href="{% url 'register' %}">Sing Up Now</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

- After the user enter the correct user and password - log success
  Django need to route the user to one page -> home.html
    - setting.py -> LOGIN_REDIRECT_URL = 'blog-home'
    

- Modify the users/views.py - after a successfully registered the user
  we can redirecting them to the login page.
```
    messages.success(request, f'Your account has been created!. You are able to log in')
    return redirect('login')
```

- created a file users/templates/users/logout.html

```
{% extends "blog/base.html" %}
{% block content %}
    <h2>You have been logged out</h2>
    <div class="border-top pt-3">
        <small class="text-muted">
            <a href="{% url 'login' %}">Log In Again</a>
        </small>
    </div>
{% endblock content %}
```

- Create a page for user profile
    - in the users/views.py
```
def profile(request):
    return render(request, 'users/profile.html')
```

- created a file users/templates/users/profile.html
```
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <h1>{{ user.username }}</h1>
{% endblock content %}
```

- create the route and our URL patterns that will use this view -> urls.py
```
urlpatterns = [ ...
    path('profile/', user_views.profile, name='profile'),
```

- Add link to this page on the navegation bar-> urls.py

```
<!-- Navbar Right Side -->
<div class="navbar-nav">
    {% if user.is_authenticated %}
        <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
        <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
    {% else %}
        <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
        <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
     {% endif %}
</div>
```

- use a django decorator  -> users/views.py
```
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'users/profile.html')
```

- create a variable in the setting.py
    - LOGIN_URL = 'login'



<h2> Web App Part 8 -   </h2> 
<h3> </h3 >
 