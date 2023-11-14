class Car:
    def __init__(self, color, brand, licence_plate):
        self.color = color
        self.brand = brand
        self.licence_plate = licence_plate


    def print_attributs(self):
        print(f"kleur = {self.color}\n"
              f"merk = {self.brand}\n"
              f"nummerplaat = {self.licence_plate}")

cars = []
x = int(input("Hoeveel wagens wil u toevoegen"))
for i in range(x):
    gegevens = input("voer de kleur, merk en nummerplaat van uw wagen in, gescheiden door een komma: ")
    gegevens = gegevens.split(",")
    kleur, merk, nummerplaat = gegevens
    new_car = Car(kleur, merk, nummerplaat)
    cars.append(new_car)

for car in cars:
    car.print_attributs()

