import json, csv

data = None

with open("json_file.json", "r") as jfile:
    data = json.load(jfile)
print(data)

with open("new_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(key for key in data[0].keys())
    for item in data:
        writer.writerow(value for value in item.values())

new_worker = {
        "name": "Mikhail Olshevski",
        "birthday": "19.11.1996",
        "height": 185,
        "weight": 84,
        "car": True,
        "languages": ["Python"]
    }
filename = 'json_file.json'

with open(filename, 'r') as jfile:
    data = json.load(jfile)

data.append(new_worker)

with open(filename, 'w') as jfile:
    json.dump(data, jfile, indent=4)

with open("new_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(key for key in data[0].keys())
    for item in data:
        writer.writerow(value for value in item.values())