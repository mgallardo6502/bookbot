import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import number_of_words
from stats import number_of_characters
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    file = get_book_text(sys.argv[1])
    split_file = len(number_of_words(file))
    characters = number_of_characters(file)
    sorted_characters = sorted_list(characters)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    print(f'Found {split_file} total words')
    print('--------- Character Count -------')
    for i in range(0, len(sorted_characters)):
        if sorted_characters[i]['name'].isalpha() == True:
            print(f"{sorted_characters[i]['name']}: {sorted_characters[i]['value']}")
    print('============= END ===============')

main()