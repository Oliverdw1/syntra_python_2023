alle_wagens = {}
def nieuwe_wagen_toevoegen():
    wagen = {}
    input_merk = input("wat is het merk van de wagen? ")
    wagen["merk"] = input_merk

    input_model = input("wat is het model van de wagen? ")
    wagen["model"] = input_model

    input_bouwjaar = input("wat is het bouwjaar van de wagen? ")
    wagen["bouwjaar"] = input_bouwjaar

    input_kleur = input("wat is het kleur van de wagen? ")
    wagen["kleur"] = input_kleur

    input_prijs = input("wat is het prijs van de wagen? ")
    wagen["prijs"] = input_prijs

    return wagen

aantal_wagens = 0
while True:
    user_input = input("Wilt u een nieuwe wagen toevoegen?y/n: ")
    if user_input == "y":
        nieuwe_wagen = nieuwe_wagen_toevoegen()
        aantal_wagens += 1
        alle_wagens[f"auto {aantal_wagens}"] = nieuwe_wagen
    elif user_input == "n":
        break
    else:
        user_input = input("foute input, kies y of n")

print(alle_wagens)