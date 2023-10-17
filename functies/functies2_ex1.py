
som = 0
def getallen_vragen():
    global som
    while True:
        getal = input("Voer een getal in, of q om te stoppen: ")
        if getal == "q":
            break
        else:
            getal = int(getal)
            som += getal


getallen_vragen()
print(som)