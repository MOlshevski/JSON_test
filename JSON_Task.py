'''import json
import csv

with open('json_file.json') as f:
    data = json.load(f)

print(data)

cols = ["name", "birthday", "height", "weight", "car", "languages"]

path = "D:\Учеба\TMS\Homework\HW_Lesson6/DEMO.csv"
with open(path, 'w') as f:
    wr = csv.DictWriter(f, fieldnames = cols)
    wr.writeheader()
    wr.writerows(data)'''



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