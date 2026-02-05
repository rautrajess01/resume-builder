from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.create_resume, name='create_resume'),
    path('preview/<int:id>/', views.preview_resume, name='preview_resume'),
    path('edit/<int:id>/', views.edit_resume, name='edit_resume'),
    path('delete/<int:id>/', views.delete_resume, name='delete_resume'),
]
