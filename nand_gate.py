def nand_gate(a, b):
    if a and b:
        return False
    else:
        return True


print(nand_gate(0,0))
print(nand_gate(0,1))
print(nand_gate(1,0))
print(nand_gate(1,1))

