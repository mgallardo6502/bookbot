def number_of_words(file):
    split_flie = file.split()
    return split_flie

def number_of_characters(file):
    characters = {}
    for character in file:
        if character.lower() not in characters:
            characters[character.lower()] = 1
        else:
            characters[character.lower()] += 1
    return characters

def sort_on(dict):
    return dict['value']

def sorted_list(characters):
    list = [] 
    for character in characters:
        value = characters[character]
        dict = {'name': character, 'value': value}
        list.append(dict)
    list.sort(reverse=True, key=sort_on)
    return list