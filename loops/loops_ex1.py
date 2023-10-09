#vraag de gebruiker om een getal tussen 1 en 10 in te geven. druk dan alle voorafgaande getallen af

number = int(input("voer een getal tussen 1 en 10 in: "))

for i in range(number-1):
    print(i+1)