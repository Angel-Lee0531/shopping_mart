from django.shortcuts import render

def homepage(request):
	return render(request, 'homepage.html')

def veg_market(request):
	return render(request, 'veg_market.html')
