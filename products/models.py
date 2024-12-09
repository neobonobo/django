from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, help_text="Unit of the product, e.g., kg, pieces")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/',null=True,blank=True)

    def __str__(self):
        return f"{self.name} ({self.unit}) - {self.price_per_unit}/unit"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, help_text="Alternative text for the image")

    def __str__(self):
        return f"Image for {self.product.name}"

