from django.urls import path
from . import views

urlpatterns = [
    path('next_meal', views.next_meal),
]
