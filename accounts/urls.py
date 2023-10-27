from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('status/',views.status,name="status"),
    path('products/',views.products,name="products"),
    path('customer/<str:pk>/',views.customer,name="customer")
]