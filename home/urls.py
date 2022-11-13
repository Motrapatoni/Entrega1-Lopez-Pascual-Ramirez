from unittest.mock import patch
from zipfile import Path
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('items/', include('items.urls'), name='items'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]