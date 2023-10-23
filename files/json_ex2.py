import json

def json(filename="personen.json"):
    with open(filename, "r") as f:
        persons = json.load(f)
        return persons

persons = json()

max_age = 0
for x in persons:
    person = persons[x]
    if person["age"] > max_age:
        max_age = person["age"]