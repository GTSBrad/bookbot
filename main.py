from stats import get_num_words, letters_in_book, get_book_text, sort_chars
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_words = get_num_words(book_path)
    characters = letters_in_book(book_path)
    book = get_book_text(book_path) 
    sorted_chars = sort_chars(characters)
    

    print("============ BOOKBOT ============")
    print("Analyzing book found at" f" {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        #return f"{item['char']}: {item['count']}"
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
main()