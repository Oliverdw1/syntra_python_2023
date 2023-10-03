def oppervlakte_driehoek(b, h):
    return (b * h)/2


basis = int(input("Voer de basis is: "))
hoogte = int(input("Voer de hoogte is: "))
print(oppervlakte_driehoek(basis, hoogte))
