## This is the Simple Resume Builder app built with Django, Postgres, Docker and Jenkins

## Project Structure
resume-builder/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── builder/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── nginx/
│   └── default.conf
│
├── resume_builder/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── tailwind.css
│   ├── images/
│   ├── js/
│   ├── src/
│   └── favicon.ico
│
├── templates/
│   └── layout.html
│
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── manage.py
├── requirements.txt
└── README.md

