from rest_framework import serializers
# from backend.store.models import Product, Category
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    # fields = ['id','name','slug']
    fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only=True)

  class Meta:
    model = Product
    fields = '__all__'

