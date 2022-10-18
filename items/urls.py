from django.contrib import admin
from django.urls import path, include
from items import views

urlpatterns = [
    path('', views.items, name='items'),
    path('create-items/', views.create_item, name='create-items'),
    path('contact/', views.contact, name='contact'),
]