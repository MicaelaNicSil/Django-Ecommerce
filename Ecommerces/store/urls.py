from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('index/', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),



    path('update_item/', views.updateItem, name="update_item"),
    path('process_order', views.processOrder, name="process_order"),

    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    
    path('logout/', views.logout_request, name="logout"),


]
