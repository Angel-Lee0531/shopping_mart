from django.contrib import admin
from django.urls import path
from veg_market import views 

urlpatterns = [
    path('admin/', admin.site.urls),
	path('homepage/', views.homepage),
]
