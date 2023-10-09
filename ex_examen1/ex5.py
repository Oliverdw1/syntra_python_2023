def contains_a_and_t(string):
    if ("a" in string) and ("t" in string):
        print(string)
    else:
        print("geen a en t in de tekst")


text = input("voer een tekst in: ")
contains_a_and_t(text)