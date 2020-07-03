
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls', namespace="blog")),
    path('filters/api/', include('filters_api.urls', namespace="filters_api")),
    path('', include('front_page.urls', namespace="front_page")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)