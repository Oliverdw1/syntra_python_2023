import json
import datetime

personen = {}
verdergaan = True
i = 1
while verdergaan:
    new_name = input("voer een naam in: ")
    new_age = datetime.date(("voer een geboortedatum in: "))
    personen[f"persoon{i}"] = {"name": new_name, "age": new_age}
    verder = input("wilt u verder gaan? y/n")
    if verder == 'n':
        verdergaan = False
    i += 1

p = json.dumps(personen)
print(p)
with open("personen.json", "w") as f:
    f.write(p)