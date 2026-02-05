from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.test_view, name='index'),
]
