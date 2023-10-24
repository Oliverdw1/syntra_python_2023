def hyphen_seperated(text):
    text = text.split('-')
    text.sort()
    text = "-".join(text)
    return text


print(hyphen_seperated("green-red-yellow-black-white"))