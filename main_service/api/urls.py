from django.urls import include, path
from rest_framework.routers import DefaultRouter

from django.urls import path

from api.views import QueryViewSet

urlpatterns = [
    path('query/', QueryViewSet.as_view({'post': 'create'}), name='query'),
]
