from django.shortcuts import render
from veg_market.models import FoodTypes, Food, ShoppingCart


def homepage(request):
	return render(request, 'homepage.html')

def veg_market(request):
	return render(request, 'veg_market.html', {'foodtypes':foodtypes, 'food':food})

def place_order(request):
	return render(request, 'place_order.html', {'foodtypes':foodtypes, 'food':food})

def check_shopping_cart(request):
	if 'food' in request.POST:
		#print(type(request.POST)) # QueryDict
		#print(type(request.POST['food']) # string
		ShoppingCart.objects.create(item_name = request.POST['food'], item_quantity = int(request.POST['quantity'])) # Create variable of specified food
		#if 'quantity' in request.POST:
			#print(request.POST['quantity'])
			#print(type(request.POST['quantity']))
			#quantity = request.POST['quantity'] 
		#else:
			#print('No quantity')
	food = Food.objects.all()
	item = ShoppingCart.objects.all()
	return render(request, 'check_shopping_cart.html', {'item':item, 'food':food})


foodtypes = FoodTypes.objects.all()
food = Food.objects.all()
