from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task-index'),
    path('<str:slug>/', views.task_detail, name='task-detail')
]