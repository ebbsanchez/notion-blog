from django.contrib import admin
from django.urls import path, include
from . import views
import os
app_name = 'front_page'

urlpatterns = [
	path('', views.index, name='front_page_index')
]

if os.getenv("THIS_ENV") == "development":
	urlpatterns.append(path('test', views.test, name='test'))