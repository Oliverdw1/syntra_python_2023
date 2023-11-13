multiplier_func = lambda x: (lambda y: x * y)
doubler = multiplier_func(2)
print(doubler(5))