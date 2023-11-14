class Plant:
    def __init__(self, naam, kleur, bewatering, frequentie):
        self.naam = naam
        self.kleur = kleur
        self.bewatering = bewatering
        self.frequentie = frequentie

    def bewateren(self):
        print(f"{self.naam} heeft water gekregen!")


eucalyptus = Plant("Eucalyptus", "groen", "weinig", "wekelijks")
eucalyptus.bewateren()
