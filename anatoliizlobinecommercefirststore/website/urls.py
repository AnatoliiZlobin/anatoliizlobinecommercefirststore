from django.urls import path

from website.views import  main_page_tag, product_plates



urlpatterns = [
	path('store/', main_page_tag),
	path('', product_plates),
]
