def getallen_vragen_lijst():
    getallen = []
    while True:
        getal = input("Voer een getal in, of q om te stoppen: ")
        if getal == "q":
            break
        else:
            getal = int(getal)
            getallen.append(getal)
    return getallen


def som(getallen):
    print(sum(getallen))


def even_oneven(getallen):
    even = []
    oneven = []
    for getal in getallen:
        if getal % 2 == 0:
            even.append(getal)
        else:
            oneven.append(getal)
    print(f"de even getallen zijn: {even}")
    print(f"de oneven getallen zijn: {oneven}")


getallen = getallen_vragen_lijst()
som(getallen)
even_oneven(getallen)