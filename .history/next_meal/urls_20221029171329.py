from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('next_meal', views.tkfcs_sjcbSelectAll),
]
