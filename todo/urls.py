from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:todo_id>/', views.update_todo_is_complete, name='update_todo_is_complete')
]