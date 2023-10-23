def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_list(n):
    lijst = []
    for i in range(n):
        lijst.append(fibonacci(i))
    return lijst


def fibonacci_nr(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    while (n-2):
        c = a + b
        a = b
        b = c
        print(c, end=' ')
        n -= 1

print(fibonacci_list(10))