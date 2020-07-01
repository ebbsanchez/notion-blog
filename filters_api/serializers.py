from .models import Filter
from rest_framework import serializers


class FiltersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filter
        fields = ['name', 'demo', 'link', 'avatar', 'slug']
