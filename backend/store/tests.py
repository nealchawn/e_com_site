from decimal import Decimal
from django.test import TestCase
from .models import Category, Product

# Create your tests here.
class CategoryModelTest(TestCase):
  def test_category_model_exists(self):
    category = Category.objects.count()

    self.assertEqual(category, 0)

class ProductModelTest(TestCase):
  #def test_build_name_slug_class_method(self):
  #  result = Product.build_name_slug("4 pack Bulb", "electronics")
  #  self.assertEqual(result, "4-pack-bulb-electronics")

  def test_cool_name_instance_method(self):
    category = Category.objects.create(
      name="Electronics",
      slug="electronics",
    )

    product = Product.objects.create(
      category=category,
      name="4 pack Bulb",
      description="4 pack of Bulb 60 W",
      price=Decimal("7.00"),
    )

    self.assertEqual(product.cool_name(), "4-pack-bulb-electronics")