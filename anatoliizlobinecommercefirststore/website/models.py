from django.db import models
from django import forms

class DataMain(models.Model):
	group = models.CharField(max_length=30, null=True)
	name = models.CharField(max_length=200, null=True, unique=True)
	number = models.CharField(max_length=300, null=True)
	description = models.TextField(null=True)
	image = forms.ImageField()
	price = models.FloatField(max_length=10)
	views_main_page = models.BooleanField(default=False)
	stock_bool = models.BooleanField(default=False)
	stock_int = models.IntegerField(null=True)
class TagMainPage(models.Model):
	tag_main_page = models.CharField(max_length=30)