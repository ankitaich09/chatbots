import json


with open('drugs.json', 'r') as jf:
    data = json.load(jf)


def find_alias_match(input_string, json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for item in data.keys():
        if "aliases" in data[item] and input_string in data[item]["aliases"]:
            return item

    return None  # Return None if no match is found


# Example usage
input_string = "2ai"
json_file_path = "drugs.json"
result = find_alias_match(input_string, json_file_path)

if result:
    print(result)
else:
    print("No match found")