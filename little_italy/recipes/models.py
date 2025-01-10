from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model): # Info: https://developer.edamam.com/edamam-docs-recipe-api
    name = models.CharField(max_length=255)
    image = models.URLField()
    healthLabels = models.TextField()
    cuisineType = models.TextField()
    calories = models.FloatField()
    totalNutrients = models.JSONField()
    ingredients = models.TextField()
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    fats = models.FloatField()
    proteins = models.FloatField()
    carbohydrates = models.FloatField()

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    size = models.CharField(max_length=20, choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('preparing', 'Preparing'),
        ('on_the_way', 'On the Way'),
        ('delivered', 'Delivered')
    ], default='preparing')

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.pizza.name}"