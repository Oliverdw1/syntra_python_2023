import random
steden = ["kortrijk", "Gent", "Antwerpen", "Mechelen", "Kluisbergen", "Brussel", "Brugge", "Sint Niklaas", "Bornem", "Luik", "Charleroi"]


def streepjes(string):
    new_string = ""
    for i in string:
        new_string += '-'
    return new_string
#print("-"*len(string))


def sterretjes(string):
    new_string = ""
    for i in string:
        new_string += '*'
    return new_string
#print("*"*len(string))


indexes = random.sample(range(len(steden)),3)
for i in indexes:
    if i % 2 == 0:
        steden[i] = streepjes(steden[i])
    else:
        steden[i] = sterretjes(steden[i])

print(indexes)
print(steden)
#enumerate