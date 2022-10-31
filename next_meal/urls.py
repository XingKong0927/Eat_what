from django.urls import path
from . import views

urlpatterns = [
    path('home', views.next_meal0),
    path('run', views.next_meal),
    path('enter', views.enter_meal),
]
