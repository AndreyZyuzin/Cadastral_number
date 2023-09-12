from django.urls import include, path

from django.urls import path

from api.views import result, ping

urlpatterns = [
    path('result/', result),
    path('', ping),
]
