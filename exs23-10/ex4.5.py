
def perfect_number(n):
    proper_divisor = []
    if n % 2 == 0:
        for i in range(int(n/2)):
            i = i + 1
            if n % i == 0:
                proper_divisor.append(i)
        if sum(proper_divisor) == n:
            print(proper_divisor)
            return True
    return False



for i in range(30):
    print(i, perfect_number(i))