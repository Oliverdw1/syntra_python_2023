def woorden(woord):
    global counter
    if woord == list(woordenboek1)[counter]:
        print("toppie woppie", woord)
        return True
    else:
        counter += 1
        if counter == len(woordenboek1):
            print("oeioei kapotiewottie")
            return False
        woorden(woord)



if __name__ == '__main__':
    woordenboek1 = {"python": "Een hoog-niveau programmeertaal.", "recursie": "Een functie die zichzelf aanroept in de definitie"}
    while True:
        counter = 0
        invoer = input("Voer woorden in (gescheiden door een spatie) of typ 'stop' om te beëindigen: ")
        if invoer == "stop":
            print(woordenboek1)
            break
        elif woorden(invoer):
            print(invoer)
            print(f"{invoer}: {woordenboek1[invoer]}")
        else:
            betekenis = input(f"Betekenis van {invoer} niet gevonden. Voer de betekenis in:\n{invoer}: ")
            woordenboek1[invoer] = betekenis

