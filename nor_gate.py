def nor_gate(a, b):
    if a or b:
        return False
    else:
        return True


print(nor_gate(0,0))
print(nor_gate(0,1))
print(nor_gate(1,0))
print(nor_gate(1,1))