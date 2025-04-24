import requests

# Reemplaza con tu propia clave API
API_KEY = 'C3CBx7//p4vPx+kqw1cy3g==Y4BTVgst6mrO6j1B'


def fetch_data(animal_name):
    """Fetch animal data from the API based on animal name"""
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        'X-Api-Key': API_KEY  # Encabezado con tu clave API
    }

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(f"{url}?name={animal_name}", headers=headers)

        # Comprobar si la respuesta fue exitosa
        if response.status_code == 200:
            # Si la respuesta es válida, devolver el JSON
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        # Captura cualquier error durante la solicitud
        print(f"Request failed: {e}")
        return None
