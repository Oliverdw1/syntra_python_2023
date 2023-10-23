import json

personen = {}
verdergaan = True
i = 1
while verdergaan:
    new_name = input("voer een naam in: ")
    new_age = input("voer een leeftijd in: ")
    personen[f"persoon{i}"] = {"name": new_name, "age": new_age}
    verder = input("wilt u verder gaan? y/n")
    if verder == 'n':
        verdergaan = False
    i += 1
print(personen)
p = json.dumps(personen)
print(p)
with open("personen.json", "w") as f:
    f.write(p)