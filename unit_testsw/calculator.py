import re
class Calculator():
    def print_string(self, string):
        return string

    def add(self, string):
        # delimiters = ",\n"
        # indeces = []
        if not string or string == "0":
            return 0
        string.find()
        # for i in len(string):
        #     if string[i] in delimiters:
        #         indeces.append(i)
        list_of_strings = string.replace("\n",",").split(",")
        list_of_ints = [int(i) for i in list_of_strings]
        return sum(list_of_ints)


calculator = Calculator()
calculator.print_string(string="hello")
