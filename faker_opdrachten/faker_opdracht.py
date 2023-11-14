from faker import Faker
import random as rd
from OO.oefeningen1.person import Person

fake = Faker("nl_BE")


def generate_city():
    cities = {}
    for i in range(10):
        city = fake.city()
        cities[city] = generate_street()
    return cities


def generate_street():
    streets = {}
    for i in range(10):
        street = fake.street_name()
        streets[street] = generate_housenumbers()
    return streets

def generate_housenumbers():
    nummers = {}
    for i in range(10):
        nummer = rd.randint(1,100)
        nummers[nummer] = {}
    return nummers

def generate_people():
    inwoners = []
    woman_first_name = fake.firstname_female()
    woman_last_name = fake.lastname()
    woman_age = rd.randint(18,99)
    inwoners.append(Person(woman_first_name,woman_last_name,woman_age))
    if 18 <= woman_age <= 60:
        if rd.random>0.5:
            

steden = generate_city()

def print_steden_lijst(steden):
    for stad in steden:
        print(f"{stad}:: ")
        for straat in steden[stad]:
            print(f"    {straat}: ")
            print("\t\t", end="")
            for nummer in steden[stad][straat]:
                print(nummer, end=', ')
            print()
        print()

print_steden_lijst(steden)