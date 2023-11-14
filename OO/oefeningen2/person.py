from datetime import datetime, timedelta
class Person:
    def __init__(self, first_name, last_name, birthdate, birth_place):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.birth_place = birth_place

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def print_attributes(self):
        print(f"Uw naam is {self.first_name} {self.last_name} en u bent {self.calculate_age()} jaar oud")
        print(f"U bent geboren op {self.birthdate} te {self.birth_place}")
        print(f"U bent 18 jaar geworden op {self.birthdate.replace(year= self.birthdate.year + 18)}")
        pensioen_leeftijd = self.birthdate.replace(year= self.birthdate.year + 68)
        print(f"U mag op pensioen in het jaar {pensioen_leeftijd.year} in de maand {pensioen_leeftijd.strftime('%B')} ")



# gegevens = input("voor uw voornaam, naam, geboortedatum en geboorteplaats in, gescheiden door een komma en een spatie: ")
gegevens = "Oliver, de Worm, 2002-11-29, Bonheiden"
gegevens = gegevens.split(", ")
voornaam, naam, geboortedatum, geboorteplaats = gegevens
geboortedatum = datetime.strptime(geboortedatum, "%Y-%m-%d").date()
p1 = Person(voornaam, naam, geboortedatum, geboorteplaats)
p1.print_attributes()
