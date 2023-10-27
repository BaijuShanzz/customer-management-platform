from django.shortcuts import render
from .models import *
# Create your views here.

def main(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status= 'Deliverd').count()
    pending = orders.filter(status= 'pending').count()
    context = {'orders':orders,'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'accounts/dashboard.html',context)

def status(request):
    return render(request, 'accounts/status.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer':customer, 'orders':orders,'order_count':order_count }
    return render(request, 'accounts/customer.html',context)