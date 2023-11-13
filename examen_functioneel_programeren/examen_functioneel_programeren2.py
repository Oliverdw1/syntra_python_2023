def woorden_checken(*words):
    """Deze functie kijkt na of het eerste argument een key is, als dat zo is, print hij de key en de betekenis
    als dat niet zo is, vraagt hij om een betekenis, daarna gaat hij recursief verder met het volgende woord
    Als de woorden op zij, stopt de functie"""
    if not words:
        return False
    if words[0] not in woordenboek1:
        betekenis = input(f"Betekenis van {words[0]} niet gevonden. Voer de betekenis in: ")
        woordenboek1[words[0]] = betekenis
    else:
        print(f"{words[0]}: {woordenboek1[words[0]]}")
    return woorden_checken(*words[1:])


def print_woordenboek(dictionary):
    """deze functie print het woordenboek op een mooie manier"""
    print("\nHuidig woordenboek:")
    for key in dictionary:
        print(f"{key}: {dictionary[key]}")
    print("\n")


if __name__ == '__main__':
    woordenboek1 = {"python": "Een hoog-niveau programmeertaal.",
                    "recursie": "Een functie die zichzelf aanroept in de definitie"}
    while True:
        invoer = input("Voer woorden in (gescheiden door een spatie) of typ 'stop' om te beëindigen: ")
        if invoer == "stop":
            print_woordenboek(woordenboek1)
            break
        woorden = invoer.split(" ")
        woorden_checken(*woorden)
        print_woordenboek(woordenboek1)