from django.shortcuts import render
from veg_market.models import FoodTypes, Food

def homepage(request):
	return render(request, 'homepage.html')

def veg_market(request):
	foodtypes = FoodTypes.objects.all()
	food = Food.objects.all()
	return render(request, 'veg_market.html', {'foodtypes':foodtypes, 'food':food})
