import os
from dotenv import load_dotenv
import data_fetcher  # Importa el módulo de data_fetcher

# Cargar las variables de entorno (si las tienes en un .env)
load_dotenv()

API_KEY = os.getenv('API_KEY')

def serialize_animal(animal_obj):
    """Convert a single animal object to HTML string"""
    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["characteristics"]["diet"].capitalize()}<br/>\n'
    output += f'    <strong>Location:</strong> {animal_obj["locations"][0].capitalize()}<br/>\n'

    if "type" in animal_obj["characteristics"]:
        output += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"].capitalize()}<br/>\n'

    if "slogan" in animal_obj["characteristics"]:
        output += f'    <strong>Slogan:</strong> {animal_obj["characteristics"]["slogan"].capitalize()}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output

def main():
    # Cargar la plantilla HTML
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        html_template = template_file.read()

    # Pedir al usuario el nombre del animal
    animal_name = input("Please enter an animal: ")

    # Obtener los datos del animal usando data_fetcher
    data = data_fetcher.fetch_data(animal_name)

    if not data:
        # Si no se encuentran animales, mostrar un mensaje
        output = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    else:
        # Generar el HTML para cada animal
        output = ""
        for animal in data:
            output += serialize_animal(animal)

    # Reemplazar el marcador de posición con el HTML de los animales
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Guardar el resultado en un archivo
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(html_output)

    print("✅ HTML file has been created successfully!")

# Ejecutar main solo si el script es ejecutado directamente
if __name__ == "__main__":
    main()
