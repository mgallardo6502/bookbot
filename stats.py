def get_book_text(book):
    return book.read()

def word_count(book):
    return len(book.split())

def characters_count(book):
    dictionary = {}
    for words in book:
        for character in words.lower():
            if character not in dictionary:
                dictionary[character] = 1
            else:
                dictionary[character] += 1
    return dictionary

def characters_sort(list):
    new_list = []
    for character in list:
        amount = list[character]
        new_list.append({"char" : character, "num" : amount})
    return new_list

def sort_on(items):
    return items["num"]