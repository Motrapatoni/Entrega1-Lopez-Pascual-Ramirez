from django.contrib import admin
from django.urls import path
from items import views

urlpatterns = [
    path('', views.Items.as_view(), name='items'),
    path('create-items/', views.create_item, name='create-items'),
    path('contact/', views.contact, name='contact'),
]