def fizzbuzz(getal,a=3,b=5):
    answer = ""
    if is_multiple(getal,a):
        answer += "fizz"
    if is_multiple(getal,b):
        answer += "buzz"
    return getal if not answer else answer


def is_multiple(number, base):
    return number % base == 0


for i in range(0,-100,-1):
    print(fizzbuzz(i))