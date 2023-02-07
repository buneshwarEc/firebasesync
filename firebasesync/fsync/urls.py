from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('student/', StudentView.as_view(), name='Drain'),
    path('student/<str:id>/', StudentView.as_view(), name='Drain'),
]