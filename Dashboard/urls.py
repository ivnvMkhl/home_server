from django.urls import path

from .views import index as dashboard

urlpatterns = [
    path('', dashboard)
]