import json
import csv

# Load the JSON file
with open('drugs.json', 'r') as file:
    substances_data = json.load(file)

# Create a CSV file
with open('substances.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write headers
    csvwriter.writerow(['Questions', 'Answers'])

    for name, substance in substances_data.items():
        aliases = substance.get('aliases', [])
        categories = substance.get('categories', [])
        formatted_effects = substance.get('formatted_effects', [])
        formatted_dose = substance.get('formatted_dose', {}).get('Oral', {})
        properties_summary = substance.get('properties', {}).get('summary', '')

        # Generate and write questions and answers
        for alias in [name] + aliases:
            dosage_answer = (
                f"The common dosage is {formatted_dose.get('Common', '')}, "
                f"the light dose is {formatted_dose.get('Light', '')}, "
                f"and the strong dose is {formatted_dose.get('Strong', '')}."
            )
            side_effects_answer = (
                f"The commonly reported side effects of {alias} are: {', '.join(formatted_effects)}"
            )
            csvwriter.writerow(['What is ' + alias + '?', properties_summary])
            csvwriter.writerow(['Tell me about ' + alias + '.', properties_summary])
            csvwriter.writerow(['What is the dosage of ' + alias + '?', dosage_answer])
            csvwriter.writerow(['What are the side effects of ' + alias + '?', side_effects_answer])

print("CSV file created successfully.")
