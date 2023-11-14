class Kamer:
    def __init__(self, lengte, breedte, hoogte):
        self.lengte = lengte
        self.breedte = breedte
        self.hoogte = hoogte

    def oppervlakte(self):
        return self.breedte * self.lengte

    def volume(self):
        return self.oppervlakte() * self.hoogte


k1 = Kamer(5,6,3)
k2 = Kamer(10,5,4)
print(k1.oppervlakte(), k1.volume())
print(k2.oppervlakte(), k2.volume())