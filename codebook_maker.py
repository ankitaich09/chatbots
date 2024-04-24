import json

#global

with open('drugs.json', 'r') as jfp:
    data = json.load(jfp)

def get_all_categories():
    all_cats = []

    for each_drug in data.keys():
        try:
            for each_c in data[each_drug]['categories']:
                all_cats.append(each_c)
        except:
            continue

    cats = list(set(all_cats))
    return cats


for each_drug in data.keys():
    official_name = each_drug
    aliases = data[each_drug]['aliases']
    categories = data[each_drug]['categories']