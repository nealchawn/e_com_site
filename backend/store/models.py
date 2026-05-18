from unicodedata import category

from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='products/', blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  #@classmethod
  def cool_name(self):
    return f"{slugify(self.name)}-{self.category.slug}"

  def __str__(self):
    return self.name
  
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=15, blank=True)
  address = models.TextField(blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    # return self.name
    # return f"Order {self.id} by {self.user.username}"
    return f"Order {self.id}"
  
class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=0)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.quantity} x {self.product.name}"
  
  
