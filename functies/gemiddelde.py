input_list = []


def gemiddelde(list):
    gemiddelde = sum(list)/len(list)
    return gemiddelde


def input_vragen():
    while True:
        invoer = input("voer een getal in: ")
        if invoer == "Q":
            break
        input_list.append(int(invoer))


input_vragen()
print(gemiddelde(input_list))