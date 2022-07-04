
from django.urls import path, include
from .views import *
from . import views  

urlpatterns = [
    path('home/', views.home, name="home"),
    path('product/', views.product, name="products"),
    path('customer/', views.customer, name="customer"),

]
