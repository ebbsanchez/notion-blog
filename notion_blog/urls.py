
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls', namespace="blog")),
    path('filters/api/', include('filters_api.urls', namespace="filters_api")),
    path('', include('front_page.urls', namespace="front_page")),
]