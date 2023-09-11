

from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home),
    path('allItems',views.allitem,name='allitems'),
    path('surf',views.surf,name='surf'),
    path('cart',views.cart,name='cart'),
    path('payment',views.make_payment,name='payment'),
     path('filter',views.filter_price,name='filter'),
]
