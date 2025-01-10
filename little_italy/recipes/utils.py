import requests
from django.conf import settings

APP_ID = settings.EDAMAM_RECIPE_APP_ID
APP_KEY = settings.EDAMAM_RECIPE_APP_KEY
BASE_URL = "https://api.edamam.com/api/nutrition-details"

def fetch_nutrition(title, ingredients):
    """
    Fetches nutrition data from the Edamam Nutrition Details API.
    
    :param title: Nombre del plato o receta.
    :param ingredients: Lista de ingredientes en formato texto.
    :return: JSON con datos nutricionales.
    """
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "title": title,
        "ingr": ingredients
    }

    response = requests.post(BASE_URL, headers=headers, json=body, params={
        "app_id": APP_ID,
        "app_key": APP_KEY
    })

    # Log para depuración
    print(f"Request URL: {response.url}")
    print(f"Request body: {body}")
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text[:500]}")  # Solo muestra los primeros 500 caracteres

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

