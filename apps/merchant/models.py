from django.db import models
from helper.models import TimeStampedModel

# Create your models here.
class Merchant(TimeStampedModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Store(TimeStampedModel):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6),
    lon = models.DecimalField(max_digits=9, decimal_places=6),
    
    def __str__(self):
        return self.name

class Catalog(TimeStampedModel):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=6),
    
    def __str__(self):
        return self.title