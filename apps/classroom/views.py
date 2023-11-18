from django.shortcuts import render

# Create your views here.

from .models import Classroom
from rest_framework import viewsets
from .serializer import ClassroomSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer