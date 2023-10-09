#vraag de gebruiker om een getal tussen 1 en 60 in te geven. Druk dan alle xijfers af die je kan delen door 9.
number = int(input("voer een getal tussen 1 en 60 in: "))

for i in range(number):
    j = i + 1
    if j % 9 == 0:
        print(j)
