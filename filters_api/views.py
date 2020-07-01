
from .models import Filter
from rest_framework import viewsets
from .serializers import FiltersSerializer


class FiltersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Filter.objects.all().order_by('-created')
    serializer_class = FiltersSerializer

