import requests
from django.conf import settings

APP_ID = settings.EDAMAM_RECIPE_APP_ID
APP_KEY = settings.EDAMAM_RECIPE_APP_KEY
BASE_URL = "https://api.edamam.com/api/nutrition-details"

def fetch_recipes(query):
    """
    Fetches nutrition data from the Edamam Nutrition API.
    """
    headers = {
        "Content-Type": "application/json"
    }
    # El cuerpo debe incluir los ingredientes en formato JSON
    body = {
        "title": query,
        "ingr": [
            "1 large pizza",
            "100g mozzarella cheese",
            "50g tomato sauce"
        ]
    }

    response = requests.post(BASE_URL, headers=headers, json=body, params={
        "app_id": APP_ID,
        "app_key": APP_KEY
    })

    print(f"Request URL: {response.url}")
    print(f"Request body: {body}")
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
