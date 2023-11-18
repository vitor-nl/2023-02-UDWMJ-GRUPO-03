from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'course'

router = routers.DefaultRouter()
router.register('cursos', views.ProductViewSet, basename='cursos')

urlpatterns = [
    path('', include(router.urls) )
]