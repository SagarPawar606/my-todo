from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task-index'),
    path('task/<str:slug>/', views.task_detail, name='task-detail'),
    path('task/<str:slug>/delete/', views.task_delete, name='task-delete')
]