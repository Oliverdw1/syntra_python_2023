getallen = []

for i in range(5):
    getal = int(input("voer een getal in tussen 1 en 10: "))
    getallen.append(getal)
    print(f"{getal}:")
    for j in range(1, getal):
        if j % 3 == 0:
            print(j)
print(getallen)