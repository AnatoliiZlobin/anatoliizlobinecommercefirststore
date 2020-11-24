from django.shortcuts import render

from .models import *

def store(request):
	return render(request, './store/store.html', {'tag': TagMainPage.objects.all()} )
