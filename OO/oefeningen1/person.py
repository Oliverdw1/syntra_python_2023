class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def main():
    gegevens = input("voor uw voornaam, naam en leeftijd in, gescheiden door een komma: ")
    gegevens = gegevens.split(",")
    voornaam, naam, leeftijd = gegevens
    p1 = Person(voornaam, naam, int(leeftijd))
    print(f"voornaam: {p1.first_name}\nnaam: {p1.last_name}\nleeftijd: {p1.age}")


if __name__ == '__main__':
    main()