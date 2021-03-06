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
 ── blog
│   ├── migrations
│    │   └── __pycache__
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

```
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
    
<h2> Web App Part 8 -  User Profile and Picture  </h2> 
<h3> We are going to implement profile page and upload the profle picture for our users</h3 >
    
- in the users/models.py 

```
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # relationship is going to be onetoone
    # on_delete=Models.CASCADE => if user is deleted the profile is going to be deleted too.
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    image = models.ImageField(default='defaults.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
```

- in the terminal execute 
    - __(django_project) django_project $ mng makemigrations__
        - ERRORS:
        - Cannot use ImageField because Pillow is not installed.
        - HINT:  run command __"python -m pip install Pillow"__.

- (django_project) django_project $ __pipenv install Pillow__

- (django_project) django_project $ mng makemigrations
```
Migrations for 'users':
  users/migrations/0001_initial.py
    - Create model Profile
```

- (django_project) django_project $ __mng migrate__
```
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions, users
Running migrations:
  Applying users.0001_initial... OK

```

- file users/admin.py -> register the page profile
```
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```

- to access Django shell
```
>>> from django.contrib.auth.models import User
>>> user = User.objects.filter(username='Plautz').first()
>>> user
<User: Plautz>
>>> user.profile
<Profile: Plautz Profile>
>>> user.profile.image
<ImageFieldFile: profile_pics/20170316_151710_yASenSJ.jpg>
>>> user.profile.image.width
2576
==> Location of image
>>> user.profile.image.url
'profile_pics/20170316_151710_yASenSJ.jpg'
>>> user = User.objects.filter(username='Gabriela').first()
>>> user
<User: Gabriela>
>>> user.profile.image
<ImageFieldFile: defaults.jpg>
```

- in setting.py file insert
  - > MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  - > MEDIA_URL = '/media/'

- in user/templates/users/profile.html
```
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <div class="media">
            <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
            <div class="media-body">
                <h2 class="account-heading">{{ user.username }}</h2>
                <p class="text-secondary">{{ user.email}}</p>
            </div>
        </div>
        <!-- FORM HERE -->
    </div>
{% endblock content %}
```

- in the project urls.py file insert
```
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, dociment_root=settings.MEDIA_ROOT)
```

- users pictures => media/profile_pics/
- defaults pictures => media/ 

- create in users/ a file signals.py
```
from django.db.models.signals import post_save
from django.contrib.auth.models import User     # sender
from django.dispatch import receiver
from .models import Profile     # create a profile and function

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

- in the users/apps.py => __take care because the user must have profile.__
```
    def ready(self):
        import users.signals
```

<h2> Web App Part 9 -  Update User Profile  </h2> 
<h3> We are going to FINISH THE USER profile page and upload the profIle picture for our users</h3 >

- file users/forms.py -> we rae going to create a Model form 
```
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
```

- in the view.py 
```
from .forms import UserRegisterForm. UserUpdateForm, ProfileUpdateForm
@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = { 
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
```

- in the file users/templates/users/profile.html
```
        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Profile Info</legend>
                {{ u_form|crispy }}
                {{ p_form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Update</button>
            </div>
        </form>
```

- route correctly in the file users/views.py
```
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.profile)
        if form.is_valid(): and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.profile)

```

- Automatically resize images when we upload them. But the largest image
  in this site right now and the CSS is set to like 125 pixels
  import the PILLOW Library

- in users/models.py
```
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
```

<h2> Web App Part 10 - Create, Update, and Delete Posts  </h2> 
<h3> We are going to study - Class-Based Views</h3 >

- the most important change occurred in the views module and in the templates too.


<h2> Web App Part 11 - Pagination  </h2> 
 - Method to insert lines in the Blog_post table
 
  ```
  >>> import json
  >>> with open('posts.json') as f:
  ...   posts_json = json.load(f)
  ... 
  >>> for post in posts_json:
  ...   post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
  ...   post.save()
  ```

<h3> Pagination procedure example  </h3> 

```
(django_project) django_project $ mng shell
Python 3.8.0 (default, Feb  3 2020, 16:24:25) 
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.paginator import Paginator
>>> posts = ['1', '2', '3', '4', '5']
>>> p = Paginator(posts, 2)
>>> p.num_pages
3
>>> for page in p.page_range:
...   print(page)
... 
1
2
3
>>> p1 = p.page(1)
>>> p1
<Page 1 of 3>
>>> p1.number
1
>>> p1.object_list
['1', '2']
>>> p1.has_previous()
False
>>> p1.has_next()
True
>>> p1.next_page_number()
2
```  

- <h2>To access some page</h2>
  - http://localhost:8000/?page=1
  
- <h2>Code inserted into blog/home.html</h2>
```
    {% if is_paginated %}
        {% if page_obj.has_previous %}
            <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
                <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
             {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
            <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    {% endif %}
{% endblock content %}
```