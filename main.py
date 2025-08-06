import sys
from stats import get_book_text
from stats import word_count
from stats import characters_count
from stats import characters_sort
from stats import sort_on

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    with open(sys.argv[1]) as f:
        book_as_string = get_book_text(f)
        amount_of_words = word_count(book_as_string)
        new_dictionary = characters_count(book_as_string)
        sorted_list = characters_sort(new_dictionary)
        sorted_list.sort(reverse=True, key=sort_on)
        
        print("============ BOOKBOT ============")
        print(f"Analysing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {amount_of_words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
        
main()