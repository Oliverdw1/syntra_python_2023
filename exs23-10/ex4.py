def string_to_dict(text) -> dict:
    new_dict = {}
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.split()
    for word in text:
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1
    return new_dict


print(string_to_dict("This is the first sentence. This is the scecond sentence. "
               "This is not the fourth sentence, it is the third sentence."))
