from django.db import models
from products.models import Product

class Additional(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='additionals')
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
