def goLeft():
    print("Left")


def goRight():
    print("Right")


def goUp():
    print("Up")


def goDown():
    print("Down")


richting = input("Geef een richting: ")
if richting == "Left":
    goLeft()
elif richting == "Right":
    goRight()
elif richting == "Up":
    goUp()
elif richting == "Down":
    goDown()
else:
    print("foute input")
