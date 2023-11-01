from django.shortcuts import render,redirect
from .models import *
from .forms import orderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
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
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders= myFilter.qs
    context = {'customer':customer, 'orders':orders,'order_count':order_count,'myFilter':myFilter }
    return render(request, 'accounts/customer.html',context)


def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form = orderForm(initial={'customer':customer})
    if request.method == 'POST':
        # we can pass the request server data into the form
        # form = orderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        
    context={'formset': formset}
    return render(request,"accounts/order_form.html",context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = orderForm(instance=order)

    if request.method == 'POST':
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request,"accounts/order_form.html",context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request,'accounts/delete.html',context)