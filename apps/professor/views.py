from django.shortcuts import render
from .models import Professor
from rest_framework import viewsets
from .serializer import ProfessorSerializer


# Create your views here.

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer  
    