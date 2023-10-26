from django.urls import path
from . import views
from .views import create_user

urlpatterns = [
    path('', views.login_view, name='login'),
    path('task_list', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/', views.view_task, name='view_task'),
    path('<int:task_id>/update_status/', views.update_status, name='update_status'),
    path('create_user/', create_user, name='create_user'),
]