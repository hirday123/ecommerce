from django.db import models
from django.contrib.auth.models import User
from .managers import MYManager

class Item(models.Model):
    name=models.CharField(max_length=40)
    Image=models.ImageField(upload_to='product/my products')
    price=models.FloatField()
    quantity=models.IntegerField()
    available=models.BooleanField(default=True)
    desc=models.TextField()
    objects = models.Manager() # by default
    products = MYManager() # filter apply
    # Item.products.get_product()


class SurfItem(models.Model):
    name=models.CharField(max_length=40)
    Image=models.ImageField(upload_to='product/Surf')
    price=models.FloatField()
    quantity=models.IntegerField()
    available=models.BooleanField(default=True)
    desc=models.TextField()
    objects = models.Manager()
    products = MYManager()


class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cat=models.CharField(max_length=40)
    cat_id=models.IntegerField()
    purchased_quan=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)




