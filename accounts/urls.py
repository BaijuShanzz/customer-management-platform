from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('status/',views.status,name="status"),
    path('products/',views.products,name="products"),
    path('customer/',views.customer,name="customer")
]