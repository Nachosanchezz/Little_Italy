from recipes.utils import fetch_nutrition
from recipes.models import Pizza, Ingredient
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Fetch nutrition details and save them to the database."

    def handle(self, *args, **kwargs):
        try:
            # Define los ingredientes de prueba
            pizzas = [
                {
                    "title": "Margarita",
                    "ingredients": [
                        "1 large pizza base",
                        "100g mozzarella cheese",
                        "50g tomato sauce"
                    ]
                },
                {
                    "title": "Pepperoni",
                    "ingredients": [
                        "1 large pizza base",
                        "100g mozzarella cheese",
                        "50g tomato sauce",
                        "50g pepperoni"
                    ]
                }
            ]

            for pizza_data in pizzas:
                title = pizza_data["title"]
                ingredients = pizza_data["ingredients"]

                # Llama a la API
                nutrition_data = fetch_nutrition(title, ingredients)

                # Crea la pizza en la base de datos
                pizza, created = Pizza.objects.update_or_create(
                    name=title,
                    defaults={
                        "description": f"Pizza {title} con ingredientes personalizados",
                        "price": 10.00,  # Precio fijo para este ejemplo
                    }
                )

                # Agrega los ingredientes con la información nutricional
                for ingredient_text in ingredients:
                    ingredient, _ = Ingredient.objects.get_or_create(
                        name=ingredient_text,
                        defaults={
                            "calories": nutrition_data.get("calories", 0),
                            "fats": nutrition_data.get("totalNutrients", {}).get("FAT", {}).get("quantity", 0),
                            "proteins": nutrition_data.get("totalNutrients", {}).get("PROCNT", {}).get("quantity", 0),
                            "carbohydrates": nutrition_data.get("totalNutrients", {}).get("CHOCDF", {}).get("quantity", 0),
                        },
                    )
                    pizza.ingredients.add(ingredient)

            self.stdout.write(self.style.SUCCESS("Successfully imported pizzas with nutrition data."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
