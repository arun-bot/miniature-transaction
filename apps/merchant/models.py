from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Merchant(TimeStampedModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Store(TimeStampedModel):
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6),
    lon = models.DecimalField(max_digits=9, decimal_places=6),
    
    def __str__(self):
        return self.name