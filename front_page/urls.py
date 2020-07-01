from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'front_page'

urlpatterns = [
	path('', views.index, name='front_page_index')
]