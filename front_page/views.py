from django.shortcuts import render
from filters_api.models import Filter
# Create your views here.


def index(request):
	filters = Filter.objects.all()
    # need refactor for api
	context = {
    	'h':filters[0],
    	'hh':filters[1],
    	'hhh':filters[2]
    }
	return render(request, 'front_page/index.html', context)
