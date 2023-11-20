from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'classroom'

router = routers.DefaultRouter()
router.register('list', views.ClassroomViewSet, basename='classroom')

urlpatterns = [
    path('', include(router.urls) )
]