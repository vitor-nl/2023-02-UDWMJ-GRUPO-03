from django.shortcuts import render
from .models import Courses
from rest_framework import viewsets
from .serializer import CoursesSerializer

# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer  