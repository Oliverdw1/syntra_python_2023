# write a function that takes a variable number of arguments (with a minimum of one),
# and returns the average of these numbers

def average(*args):
    if args:
        count = len(args)
        som = sum(args)
        return som/count
    else:
        return("Moet minstens 1 getal hebben")

print(average(1,5,6,1,9,5))
print(average(0))