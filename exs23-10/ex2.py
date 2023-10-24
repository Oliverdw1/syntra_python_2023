# Write a function that returns a string based on two input arguments:
#
#   - a character or string to be repeated
#   - the number of times the string should be repeated
#
# the function should be such that the number of repetitions defaults to 10 if its not passed by
# the caller, and the default character to be repeated should be a negative sign '-'
#
# call your function seperator
# use a keyword only argument for the string argument

def seperator(string='-', rep=10):
    return string * rep


if __name__ == "__main__":
    print(seperator(string = "100"))
