from django.db import models

# Create your models here.


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    price =models.PositiveIntegerField()
    image=models.URLField()
