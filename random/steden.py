import random
steden = ["kortrijk", "Gent", "Antwerpen", "Mechelen", "Kluisbergen", "Brussel", "Brugge", "Sint Niklaas", "Bornem", "Luik", "Charleroi"]


def streepjes(string):
    new_string = ""
    for i in string:
        new_string += '-'
    return new_string


def sterretjes(string):
    new_string = ""
    for i in string:
        new_string += '+'
    return new_string


indexes = random.sample(range(11),3)
for i in indexes:
    if i % 2 == 0:
        steden[i] = streepjes(steden[i])
    else:
        steden[i] = sterretjes(steden[i])

print(steden)
