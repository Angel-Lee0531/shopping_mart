from django.contrib import admin
from django.urls import path
from veg_market import views 

urlpatterns = [
    path('admin/', admin.site.urls),
	path('homepage/', views.homepage),
	path('veg_market/', views.veg_market),
	path('place_order/', views.place_order),
	path('check_shopping_cart/', views.check_shopping_cart),
]
