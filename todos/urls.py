from django.urls import path 
from .views import ListTodo
from .views import DetailTodo

urlpatterns = [
    path('', ListTodo.as_view(), name='todos_list'),
    path('<int:pk>/', DetailTodo.as_view(), name='todos_detail'),

]