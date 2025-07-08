from stats import count_words, letters_to_list, letter_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_location = sys.argv[1]
    book = get_book_text(book_location)
    word_count = count_words(book)
    letters = letter_count(book)
    letters_list = letters_to_list(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter in letters_list:
        if letter["char"].isalpha() == True:
            print(f"{letter["char"]}: {letter["num"]}")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()