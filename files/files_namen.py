namen = []
while True:
    nieuwe_naam = input("Voeg een naam toe: ")
    if nieuwe_naam == "q":
        break
    else:
        namen.append(nieuwe_naam)

# lijst aan file toevoegen
with open("namen.txt","w") as f:
    for naam in namen:
        f.write(naam+"\n")


# functie om nieuwe naam toe te voegen
def add_name():
    naam = input("Welke naam wilt u toevoegen?: ")
    namen.append(naam)


# functie om naam te verwijderen
def delete_name():
    naam = input("welke naam wilt u wissen?: ")
    if naam not in namen:
        print("naam staat niet in lijst kies een andere naam")
        delete_name()
    else:
        for n in namen:
            if n == naam:
                namen.remove(n)


# functie om naam te wijzigen
def change_name():
    naam = input("welke naam wilt u aanpassen?: ")
    nieuwe_naam = input("en wat moet de nieuwe naam worden?")
    if naam not in namen:
        print("naam staat niet in lijst kies een andere optie: ")
        change_name()
    else:
        for n in range(len(namen)):
            if namen[n] == naam:
                namen[n] = nieuwe_naam


while True:
    option = input("wat wil je doen? naam toevoegen/naam wissen/naam aanpassen/lijst lezen/stoppen: ")
    if option == "naam toevoegen":
        add_name()
    if option == "naam wissen":
        delete_name()
    if option == "naam aanpassen":
        change_name()
    if option == "lijst lezen":
        print(namen)
    if option == "stoppen":
        break
    with open("namen.txt", "w") as f:
        for naam in namen:
            f.write(naam + "\n")

