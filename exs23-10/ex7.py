def pangram(text):
    text = text.replace(' ','')
    text = text.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in text:
        if letter in letters:
            #print("found letter")
            letters.remove(letter)
    return letters == []

def pangram2(text):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    text = text.replace(' ','')
    return letters.issubset(set(text.lower()))

"""print(pangram("The quick brown fox jumps over the lazy dog"))
print(pangram("azertyuiopqsdfghjklmwxcvbn"))
print(pangram("aertyuiopqsdfghjklmwxcvbnaqrsdgfutybvug"))"""

print(pangram2("The quick brown fox jumps over the lazy dog"))