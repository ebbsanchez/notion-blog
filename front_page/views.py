from django.shortcuts import render
from filters_api.models import Filter
# Create your views here.


def index(request):
	return render(request, 'front_page/index.html')

def test(request):
	return render(request, 'front_page/test.html')