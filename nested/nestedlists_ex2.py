
studenten = [{"id": 12345, "naam": "de Worm", "voornaam": "Oliver", "leeftijd": 20, "cursus": "Python"},
             {"id": 6969, "naam": "Jansens", "voornaam": "Jan", "leeftijd": 25, "cursus": "IT"},
             {"id": 420, "naam": "Peeters", "voornaam": "Peter", "leeftijd": 60, "cursus": "Python"},
             {"id": 12, "naam": "Bond", "voornaam": "James", "leeftijd": 60, "cursus": "IT"},
             {"id": 3, "naam": "shit", "voornaam": "Fucking", "leeftijd": 69, "cursus": "Python"}]

leeftijden = []
ITers = []
Pythoners = []
for student in studenten:
    print(student["voornaam"], student["naam"])
    leeftijden.append(student["leeftijd"])
    if student["cursus"] == "IT":
        ITers.append(student["id"])
    if student["cursus"] == "Python":
        Pythoners.append(student["id"])
print(list(set(leeftijden)))
print(ITers)
print(Pythoners)
