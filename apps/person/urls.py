from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'person'

router = routers.DefaultRouter()
router.register('person', views.PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls) )
]