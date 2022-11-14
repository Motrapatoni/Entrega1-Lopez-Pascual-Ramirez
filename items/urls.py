from django.contrib import admin
from django.urls import path
from items import views

urlpatterns = [
    path('', views.Items.as_view(), name='items'),
    path('create-items/', views.CreateItem.as_view(), name='create-items'),
    path('read-item/<int:pkj>/',views.ReadItem.as_view() ,name='read-item'),
    path('contact/', views.contact, name='contact'),
]