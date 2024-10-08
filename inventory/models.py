from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name
