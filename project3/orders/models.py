from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} - username = {self.username}, password = {self.password}"

class Items(models.Model):
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=10)

class Toppings(models.Model):
    type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    cost = models.DecimalField(decimal_places=2,max_digits=10)

class Orders(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    # toppings = models.ForeignKey(Toppings, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - item = {self.item}"
        # return f"{self.id} - item = {self.item}, toppings = {self.toppings}"
