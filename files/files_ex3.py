with open("pythontest.txt", "a") as my_file:
    line = input("Voer een regel tekst in:\n")
    my_file.write(line)

with open("pythontest.txt", "r") as my_file:
    print(my_file.read())