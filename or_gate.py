def or_gate(a, b):
    if a and not b:
        return True
    elif not a and b:
        return True
    elif a and b:
        return True
    elif not a and not b:
        return False


def or_gate2(a, b):
    return a | b


print(or_gate(0,0))
print(or_gate(0,1))
print(or_gate(1,0))
print(or_gate(1,1))

print(or_gate2(0,0))
print(or_gate2(0,1))
print(or_gate2(1,0))
print(or_gate2(1,1))
