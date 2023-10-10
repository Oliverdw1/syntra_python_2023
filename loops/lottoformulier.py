
for i in range(9):
    for j in range(1, 6):
        print((i*5)+j, end="\t")
    print()
"""
TOTAAL = 45
AANTAL_PER_RIJ = 5

lottonummer = 1

for rij in range(int(TOTAAL / AANTAL_PER_RIJ)):
    for kolom in range(AANTAL_PER_RIJ):
        print(lottonummer, end="\t")
        lottonummer += 1
    print()
"""