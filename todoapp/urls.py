from django.urls import path
from . import views

urlpatterns = [

    path('', views.apioverview, name='apiview'),
    path('task-list/', views.tasklist, name='tasklist'),
    path('task-detail/<str:pk>/', views.task_detail, name='task_detail'),
    path('task-update/<str:pk>/', views.task_update, name='track_update'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-delete/<str:pk>', views.task_delete, name='task_delete'),

]