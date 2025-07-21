# def get_book_text(book_path):
#     with open(book_path) as file:
#         return file.read()  
from stats import get_num_words
from stats import letters_in_book

def main():
    book_path = "books/frankenstein.txt"  # Replace with your book file path
    print(f"{get_num_words(book_path)} words found in the document")
    print(f"{letters_in_book(book_path)} unique words found in the document")

main()