from django.db import models
from django.core.validators import MinValueValidator


# product models
class Product(models.Model):
    name = models.CharField(max_length=200)
    length = models.DecimalField(max_digits = 10, decimal_places=2, validators = [MinValueValidator(0.01)],)
    width = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01)],)
    height = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.01)],)
    weight = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0.001)],)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name