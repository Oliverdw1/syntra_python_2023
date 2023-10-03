def even(i):
    return i % 2 == 0


def middelste_cijfer(getal):
    midden = int(len(getal) / 2)
    if even(len(getal)):
        print(getal[midden-1: midden+1])
    else:
        print(getal[round(midden)])


invoer = input("voer een getal in: ")
middelste_cijfer(invoer)
