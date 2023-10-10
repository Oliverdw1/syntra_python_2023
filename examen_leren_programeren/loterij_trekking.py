import random
#de lijst met dieren
animals = ["stier", "vis", "dolfijn", "beer", "giraf", "hond", "muis", "orka", "octopus", "kat",
            "slang", "lama", "olifant", "pinguin", "vogel", "emoe", "koala", "paard", "zebra", "kangoeroe"]
#de computer kiest 5 willekeurige dieren
computer_choice = random.sample(animals, 5)

#ik laat de gebruiker 5 dieren kiezen
user_choice = []
for i in range(5):
    choice = input(f"kies een dier uit de volgende dieren\n{animals}\n")
    if choice not in animals:
        choice = input("Dit is geen dier uit de lijst, kies opnieuw: ")
    if choice in user_choice:
        choice = input("Dit dier heb je al gekozen, kies een ander dier: ")
    else:
        user_choice.append(choice)

#een fucntie om de gekozen dieren op een nettere manier te printen
def print_gekozen_dieren(dieren):
    output = ""
    for dier in dieren:
        output += f"{dier}, "
    return output

#maakt een lijst met de dieren van de gebruiker die ook gekozen zijn door de computer
winning_choices = []
for animal in user_choice:
    if animal in computer_choice:
        winning_choices.append(animal)


#output van de gebruiker en de computer gekozen dieren
print(f"uw gekozen afbeeldingen zijn: {print_gekozen_dieren(user_choice)}")
print(f"de winnende afbeeldingen zijn: {print_gekozen_dieren(computer_choice)}")
print(f"u heeft de volgende {len(winning_choices)} afbleeding(en) correct:  {print_gekozen_dieren(winning_choices)}")



#print de lijst met animals met de streepjes en de sterretjes op de juiste plaatsen
for animal in animals:
    if animal in winning_choices:
        print("*"*len(animal))
    elif animal in computer_choice:
        print("-"*len(animal))
    else:
        print(animal)