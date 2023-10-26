from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10,null=True)
    phone = models.BooleanField(null=True)
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

    def __str__(self):
        return self.name

