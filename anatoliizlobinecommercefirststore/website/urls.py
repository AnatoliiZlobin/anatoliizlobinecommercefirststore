from django.urls import path
from . import views
from website.views import *


urlpatterns = [
	path('', store),

]
