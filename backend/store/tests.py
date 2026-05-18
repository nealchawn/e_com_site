from django.test import TestCase
from .models import Category

# Create your tests here.
class CategoryModelTest(TestCase):
  def test_category_model_exists(self):
    category = Category.objects.count()

    self.assertEqual(category, 0)