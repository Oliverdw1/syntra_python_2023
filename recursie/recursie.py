import random


def factorial(x):
    if x == 1:
        return 1
    else: return x * factorial(x-1)


comp_number = random.randint(1, 20)
print(comp_number)


def guess_number(counter=1):
    number = int(input("kies een getal tussen 1 en 20: "))
    if number == comp_number:
        print("goed geraden!")
    elif counter >= 5:
        print(f"geen pogingen meer!\nHet juiste nummer was: {comp_number}")
    else:
        guess_number(counter+1)

def main():
    guess_number()

if __name__ == "__main__":
    main()

