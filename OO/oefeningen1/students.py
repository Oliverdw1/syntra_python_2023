class Student:
    courses = ["programmeren", "bouw", "electriciteit"]

    def __init__(self, naam, richting):
        self.naam = naam
        self.richting = richting

    @property
    def richting(self):
        return self._richting

    @richting.setter
    def richting(self, richting):
        if richting not in self.courses:
            raise ValueError(f"Richting is geen geldige optie, kies uit {self.courses}")
        self._richting = richting


s1 = Student("Oliver", "programmeren")
print(s1.naam, s1.richting)
