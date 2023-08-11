from django.contrib.auth import get_user_model
from .models import ToDo
from .serializers import ToDoSerializer

from rest_framework import viewsets

User = get_user_model()


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

