import json
import csv

with open("personen.json", "r") as j:
    persons = json.load(j)

#with open("personen.csv", "a") as c:
 #   dict_object = csv.DictWriter(c,d)
  #  dict_object.writerow(d)

def write_csv():
    with open("personen.csv", "w", newline='') as c:
        writer = csv.writer(c)
        writer.writerow(['person', 'name', 'age'])

        for person, info in persons.items():
            name = info["name"]
            age = info["age"]
            writer.writerow([person, name, age])

write_csv()