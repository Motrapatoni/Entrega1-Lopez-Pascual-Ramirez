from django.contrib import admin
from django.urls import path
from msgs import views

urlpatterns = [
    path('msgs/', views.show_msgs, name='msgs'),
]