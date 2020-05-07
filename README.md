# django_project

Python Django Tutorial: Full-Featured Web App from Corey Schafer

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
