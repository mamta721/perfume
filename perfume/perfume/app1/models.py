from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class product(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Exclusive', 'Exclusive'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="General")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')


class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class cnt(models.Model):
    fname=models.FileField(max_length=50)
    lname=models.FileField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.FileField(max_length=50)


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    total_items = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)