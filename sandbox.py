import json


with open('drugs.json', 'r') as jf:
    data = json.load(jf)


def find_alias_match(input_string, json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data.keys():
        if "aliases" in data[item] and input_string in data[item]["aliases"]:
            return {
                'Name':item,
                'Dosage':data[item]["properties"]["dose"],
                'Summary':data[item]["properties"]["summary"]
            }

    return None  # Return None if no match is found


# Example usage

def main():
    input_string = input("What are you searching for? ")
    json_file_path = "drugs.json"
    result = find_alias_match(input_string, json_file_path)
    if result:
        print(f"You wanted to search for {input_string}. This substance is officially called {result['Name']}. \n The safe dosage is {result['Dosage']} \n. Here's more about the substance :\n {result['Summary']}")
    else:
        print("No match found")

