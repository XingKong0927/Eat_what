from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('next_meal', views.next_meal),
]
