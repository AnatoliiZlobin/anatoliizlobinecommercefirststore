from django.shortcuts import render

from .models import *


def main_page_tag(request):
	return render(request, './store/store.html', {'tag': TagMainPage.objects.all()} )
def product_plates(request):
	return render(request, './store/store.html', {'product': DataMain.objects.all()} )