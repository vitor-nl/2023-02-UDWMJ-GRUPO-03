from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'person'

router = routers.DefaultRouter()
router.register('person', views.CategoryViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls) )
]