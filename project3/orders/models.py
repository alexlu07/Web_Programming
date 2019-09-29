from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - username = {self.username}, password = {self.password}"

class Beverage(models.Model):
    name = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=5)

class Salad(models.Model):
    name = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=5)

class Salad_Extras(models.model):
    name = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=5)

class Pizza(models.model):
    name = models.CharField(max_length=64)
    small_cost = models.DecimalField(decimal_places=2,max_digits=5)
    large_cost = models.DecimalField(decimal_places=2,max_digits=5)

class Pizza_Toppings(models.model):
    name = models.CharField(max_length=64)
    small_cost = models.DecimalField(decimal_places=2,max_digits=5)
    large_cost = models.DecimalField(decimal_places=2,max_digits=5)

class Sub(models.model):
    name = models.CharField(max_length=64)
    small_cost = models.DecimalField(decimal_places=2,max_digits=5)
    large_cost = models.DecimalField(decimal_places=2,max_digits=5)

class Sub_Extras(models.model):
    name = models.CharField(max_length=64)
    small_cost = models.DecimalField(decimal_places=2,max_digits=5)
    large_cost = models.DecimalField(decimal_places=2,max_digits=5)

class Pasta(models.model):
    name = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=5)

class Pasta_Extras(models.model):
    name = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=5)
