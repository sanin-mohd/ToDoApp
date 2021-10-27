from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .views import TaskDelete, TaskList,TaskDetail,TaskCreate, TaskUpdate,UpdateView,DeleteView


urlpatterns = [
    
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task_create',TaskCreate.as_view(),name='task_create'),
    path('task_update/<int:pk>/',TaskUpdate.as_view(),name='task_update'),
    path('task_delete/<int:pk>/',TaskDelete.as_view(),name='task_delete'),
    
]