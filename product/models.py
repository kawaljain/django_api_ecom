from django.db import models
from core.models import TimeStampedModel
# Create your models here.

class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    guid = models.CharField(max_length=40,unique=True)
    price = models.FloatField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    meta_keywords = models.TextField()