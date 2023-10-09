#vraag de gebruiker om 3 getallen en zet deze in een lijst
# indien het getal een even getal is deel je dit door 2 en sorteer dan de lijst
def even(i):
    return i % 2 == 0


my_list = []
for i in range(3):
    invoer = int(input("voer een getal in: "))
    if even(invoer):
        invoer /= 2
    my_list.append(int(invoer))


print(sorted(my_list))