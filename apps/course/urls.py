from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'course'

router = routers.DefaultRouter()
router.register('courses', views.CoursesViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls) )
]
