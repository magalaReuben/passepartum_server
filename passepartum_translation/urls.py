from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/translate/', views.translate, name='members'),
]