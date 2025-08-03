from stats import get_book_text
from stats import word_count
from stats import characters_count

def main():
    with open("books/frankenstein.txt") as f:
        book_as_string = get_book_text(f)
        amount_of_words = word_count(book_as_string)
        new_dictionary = characters_count(book_as_string)
        print(amount_of_words, new_dictionary)
main()