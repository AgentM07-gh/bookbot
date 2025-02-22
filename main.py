
from stats import word_count
from stats import character_count
from stats import sorted_char_count
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_string = get_book_text(book_path)
    num_words = word_count(book_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = character_count(book_string)
    sorted_chars = sorted_char_count(char_dict)
    for char in sorted_chars:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["count"]}")
    
    print("============= END ===============")


main()
