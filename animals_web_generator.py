import json

def load_data(file_path):
    """Load animal data from JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

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
    # Load the HTML template
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        html_template = template_file.read()

    # Load the animal data
    animals_data = load_data("animals_data.json")

    # Generate the HTML for each animal
    output = ""
    for fox in animals_data:
        output += serialize_animal(fox)

    # Replace the placeholder with actual animal HTML
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Save to file
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(html_output)

    print("✅ HTML file has been created successfully!")
    print(html_output)

# Only run main if this script is executed directly
if __name__ == "__main__":
    main()
