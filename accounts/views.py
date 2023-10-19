from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'accounts/main.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def status(request):
    return render(request, 'accounts/status.html')

def products(request):
    return render(request, 'accounts/products.html')