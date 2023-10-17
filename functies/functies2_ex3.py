
personen = []
def info_toevoegen(naam, salaris = 2000):
    persoon = {"naam": naam, "salaris" : salaris}
    return persoon


for i in range(5):
    invoer = input("Voer uw naam en salaris in, gespleten door een komma-teken(,): ")
    if ',' in invoer:
        naam, salaris = invoer.split(',')
        personen.append(info_toevoegen(naam, int(salaris)))
    else:
        personen.append(info_toevoegen(invoer))



print(personen)