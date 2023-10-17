merken = {
    1: "bmw",
    2: "tesla",
    3: "porsche",
    4: "mercedes",
    5: "ford"
}

for key in merken:
    print(f"Type {key} is merk {merken[key]}")
keuze = int(input("Met welk merk van wagen rijdt u? "))
print(f"U rijdt met {merken[keuze]}.")