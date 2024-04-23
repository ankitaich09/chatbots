import json


with open('drugs.json', 'r') as jf:
    data = json.load(jf)


def find_alias_match(input_string, json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data.keys():
        if "aliases" in data[item] and input_string in data[item]["aliases"]:
            temp = {
                'Name':item,
                'Dosage':data[item]["properties"]["dose"],
                'Summary':data[item]["properties"]["summary"]
            }
            return temp

    return None  # Return None if no match is found

def find_name_match(input_string, json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data.keys():
        if input_string == item:
            temp = {
                'Name':item,
                'Aliases': data[item]["aliases"],
                'Dosage':data[item]["properties"]["dose"],
                'Summary':data[item]["properties"]["summary"]
            }
            return temp

    return None  # Return None if no match is found



def print_format( input_string, result):
    string = f"You wanted to search for {input_string}. This substance is officially called {result['Name']}. \n The safe dosage is {result['Dosage']} \n. Here's more about the substance :\n {result['Summary']}"
    return string


def csv_maker():
    for keys in data.keys():
        #keys has official name
        #define a question and answer maker here
        return 0



# Example usage

def main():
    input_string = input("What are you searching for? ")
    json_file_path = "drugs.json"
    result = find_alias_match(input_string, json_file_path)
    if result:
        print(f"You wanted to search for {input_string}. This substance is officially called {result['Name']}. \n The safe dosage is {result['Dosage']} \n. Here's more about the substance :\n {result['Summary']}")
    else:
        print("No match found")

