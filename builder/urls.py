from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.create_resume, name='create_resume'),
    path('edit/<int:id>/', views.edit_resume, name='edit_resume'),
    path('delete/<int:id>/', views.delete_resume, name='delete_resume'),
]
