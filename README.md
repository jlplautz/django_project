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

# When we use (.) to creat a django project - the project is going to be create in the same directory
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
