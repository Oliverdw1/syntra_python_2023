import random
print("---Lotto---")
print("---Kies uw 6 cijfers---")
gekozen_getallen = []


for i in range(1,7):
    getal = int(input(f"Geef een getal op tussen 1 en 45(getal {i}): "))
    if 1 > getal > 45:
        getal = int(input(f"Het getal moet tussen 1 en 45 zijn, kies opnieuw: "))
    if getal in gekozen_getallen:
        getal = int(input(f"u heeft dit getal al gekozen, kies een ander getal: "))
    gekozen_getallen.append(getal)


computer_getallen = random.sample(range(1, 46), 6)
print(f"de winnende combinatie is: {computer_getallen}")
print("We gaan nu kijken of u gewonnen heeft")


winnende_getallen = set(gekozen_getallen).intersection(set(computer_getallen))

print(f"Aantal correcte cijfers: {len(list(winnende_getallen))}")
print(f"Volgende cijfers zijn correct: {list(winnende_getallen)}")
