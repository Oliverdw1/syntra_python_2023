def woorden_checken(*words):
    """Deze functie kijkt na of het eerste argument een key is, als dat zo is, print hij de key en de betekenis
    als dat niet zo is, vraagt hij om een betekenis, daarna gaat hij recursief verder met het volgende woord
    Als de woorden op zij, stopt de functie"""
    if not words:
        return False
    word, *remaining_words = words
    if word not in woordenboek1:
        betekenis = input(f"Betekenis van {word} niet gevonden. Voer de betekenis in: ")
        woordenboek1[word] = betekenis
    else:
        print(f"{word}: {woordenboek1[word]}")
    return woorden_checken(*remaining_words)


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