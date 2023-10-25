from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10,null=True)
    phone = models.BooleanField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    