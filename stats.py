def get_num_words(book_path):
    with open(book_path) as file:
        num_words = len(file.read().split())
        return num_words
    
def letters_in_book(book_path):
    num_of_letters = {}
    with open(book_path) as file:
        text = file.read()
        for letter in text:
            if letter:
                letter = letter.lower()
                if letter in num_of_letters:
                    num_of_letters[letter] += 1
                else:
                    num_of_letters[letter] = 1
    return print(num_of_letters)