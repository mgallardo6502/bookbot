def word_count(book):
    return len(book.split())

def get_book_text(book):
    return book.read()

def characters_count(book):
    dictionary = {}
    for words in book.lower():
        for character in words:
            if character not in dictionary:
                dictionary[character] = 1
            else:
                dictionary[character] += 1
    return dictionary