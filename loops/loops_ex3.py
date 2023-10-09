"""
# vraag de gebruiker om een tekst in te geven. Tel het aantal letters en cijfers en druk deze dan af
tekst = input("voer uw tekst in: ")
gebruikte_letters = []
gebruikte_cijfers = []
letters = {'a', 'b','c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
cijfers = {'1', '2','3','4','5','6','7','8','9','0'}
for teken in tekst:
    if teken.lower() in letters:
        gebruikte_letters.append(teken)
    if teken in cijfers:
        gebruikte_cijfers.append(teken)
print(gebruikte_cijfers)
print(gebruikte_letters)
"""


#simpelere versie
tekst = input("voer uw tekst in: ")
gebruikte_letters = []
gebruikte_cijfers = []
for teken in tekst:
    if teken.isalpha():
        gebruikte_letters.append(teken)
    if teken.isdigit():
        gebruikte_cijfers.append(teken)
print(gebruikte_cijfers)
print(gebruikte_letters)

