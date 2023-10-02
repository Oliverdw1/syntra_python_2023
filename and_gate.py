
def and_function(a, b):
    #a = int(input("getal a: "))
    #b = int(input("getal b: "))
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 0
    elif a== 1 and b == 0:
        return 0
    elif a == 1 and b == 1:
        return 1
def and_function2(a,b):
    if a and b:
        return True
    else:
        return False

print(and_function(0,0))
print(and_function(0,1))
print(and_function(1,0))
print(and_function(1,1))

print(and_function2(0,0))
print(and_function2(0,1))
print(and_function2(1,0))
print(and_function2(1,1))