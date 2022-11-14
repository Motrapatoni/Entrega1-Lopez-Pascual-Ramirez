from django.contrib import admin
from django.urls import path
from items import views

urlpatterns = [
    path('', views.Items.as_view(), name='items'),
    path('create-items/', views.CreateItem.as_view(), name='create-items'),
    path('read/<int:pk>', views.ReadItem.as_view(), name='read'),
    path('edit/<int:pk>', views.EditItem.as_view(), name='edit-item'),
    path('delete/<int:pk>', views.DeleteItem.as_view(), name='delete-item'),
    path('contact/', views.contact, name='contact'),
]