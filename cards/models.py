from django.conf import settings
from django.db import models

# Create your models here.

class Quemsomos(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title

class Promocoes(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class Acomodacoes(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
