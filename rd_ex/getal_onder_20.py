import random

rand_number = random.randint(1,20)
geraden = False
while not geraden:
    guess = int(input("kies een getal tussen 1 en 20, voer 999 in als je wilt stoppen: "))
    if guess == rand_number:
        print("juist!")
        geraden = True
    if guess == 999:
        print("jammer, bedankt om te spelen")
        break
    elif guess < rand_number:
        print("hoger")
    elif guess > rand_number:
        print("lager")