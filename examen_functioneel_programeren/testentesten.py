def find_matching_key(word, dictionary, *words):
    if word in dictionary:
        return word
    if not words:
        return None
    return find_matching_key(words[0], dictionary, *words[1:])

# Example dictionary
my_dict = {
    "apple": "Fruit",
    "carrot": "Vegetable",
    "dog": "Animal",
    "banana": "Fruit",
    "cat": "Animal"
}

# Words to check
words_to_check = ["apple", "car", "banana", "cat"]

for word in words_to_check:
    match = find_matching_key(word, my_dict, *words_to_check)
    if match:
        print(f"{word} matches the key: {match} with value: {my_dict[match]}")
    else:
        print(f"{word} does not match any key in the dictionary.")
