from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('update/<pk>', views.update, name='update'),
    path('remove/<pk>', views.remove, name='remove'),

]