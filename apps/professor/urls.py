from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'professor'

router = routers.DefaultRouter()
router.register('professor', views.ProfessorViewSet, basename='professor')

urlpatterns = [
    path('', include(router.urls) )
]