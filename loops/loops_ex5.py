#zonder nested loops

for i in range(1,6):
    print("*"*i)
for j in range(4, 0, -1):
    print("*"*j)

print("-------------")


def sterretjes_printen(stars):
    for i in range(1,stars*2):
        if i <= stars:
            print("*"*i)
        else:
            print("*"*(stars*2 - i))


def sterretjes_printen2(stars):
    for i in range(1,stars+1):
        print("*" * i)
    for j in range(stars-1, 0, -1):
        print("*"*j)


def sterretjes_printen3(aantal_sterren):
    for i in range(1, aantal_sterren+1):
        if i < aantal_sterren:
            print(i*"*")
        else:
            for j in range(aantal_sterren):
                print((aantal_sterren-j)*"*")
sterretjes_printen(5)
print("-------------")
sterretjes_printen2(5)
print("-------------")
sterretjes_printen3(5)