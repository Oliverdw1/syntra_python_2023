import random

worpen = 1000
beurten = []
for i in range(worpen):
    worp = random.randint(1,6)
    beurten.append(worp)
    #print(worp)

gemiddelde = sum(beurten)/worpen
print(f"gemiddelde is: {gemiddelde}")