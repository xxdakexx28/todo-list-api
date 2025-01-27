from rest_framework import generics

from .models import todos
from .serializers import TodoSerializer

# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = todos.objects.all()
    serializer_class = TodoSerializer
    
    