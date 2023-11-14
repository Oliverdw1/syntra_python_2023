import json
from OO.oefeningen1.person import Person

f = open("people.json")
data = json.load(f)
persons = {}
counter = 0
for i in data:
    for street in data[i]:
        #print(i,street)
        for nr in data[i][street]:
            #print(nr)
            for person in data[i][street][nr]:
                persons[str(counter)] = Person(person["first name"], person["last_name"], person["age"])
                counter += 1

for i in persons:
    print(f"{persons[i].first_name} {persons[i].last_name} is {persons[i].age} jaar oud. {'ouwe zak!' if persons[i].age > 30 else 'jonkie'}")