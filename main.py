import sys
from stats import count_the_words
from stats import count_the_letters


def get_book_text (filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def count_the_wordss (text_to_count):
    word_array = text_to_count.split()
    word_count = len(word_array)
    print(f"Found {word_count} total words")

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text (book_path)
    answer = count_the_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {answer} total words")
    answer = count_the_letters(book_text)
    print("--------- Character Count -------")
    for key in answer:
        print(f"{key['char']}: {key['num']}")
    print("============= END ===============")

main()
