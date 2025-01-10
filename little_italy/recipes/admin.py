from django.contrib import admin
from .models import Pizza, Ingredient

# Registrar los modelos en el admin
admin.site.register(Pizza)
admin.site.register(Ingredient)
