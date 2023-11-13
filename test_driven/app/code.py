from math import factorial


def add(a, b):
    return a + b


def reverse_string(string):
    return string[::-1]


def max_number(a, b):
    return a if a > b else b


def is_even(a):
    return a % 2 == 0


def filter_even_numbers(lijst: list):
    return list(filter(is_even, lijst))


def concatenate_strings(s1, s2):
    return s1+s2


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def factorial2(n):
    return factorial(n)


def reverse_list(lijst):
    return lijst[::-1]
