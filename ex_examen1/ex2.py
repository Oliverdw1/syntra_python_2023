def capital(string):
    return string.upper()


def lower(string):
    return string.lower()


def camel_case(string):
    return string.title()


word = input("voer uw voornaam en familienaam in: ")
print(capital(word))
print(lower(word))
print(camel_case(word))