from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY = (('Indoor', 'Indoor'),
    ('Out Door', 'Out Door'))
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100,null=True,choices=CATEGORY)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (('pending', 'pending'),
              ('Out of delivery','Out of delivery'),
              ('Deliverd','Deliverd'))
    Customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    note = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.Customer
    
    def __str__(self):
        return self.product.name