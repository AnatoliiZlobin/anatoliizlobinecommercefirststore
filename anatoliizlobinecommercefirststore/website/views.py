from django.shortcuts import render
from .models import *

def store(request):
	context = {}
	return render(request, 'store/store.html', context)
