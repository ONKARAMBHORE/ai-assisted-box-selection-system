from django.core.validators import MinValueValidator
from django.db import models

from apps.products.models import Product


# order models
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
    


# order item models

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items",)
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name="order_items",)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"