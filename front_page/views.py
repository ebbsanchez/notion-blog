from django.shortcuts import render
from filters_api.models import Filter
# Create your views here.


def index(request):
	filters = Filter.objects.all()
    # need refactor for api
	context = {}
	return render(request, 'front_page/index.html', context)
