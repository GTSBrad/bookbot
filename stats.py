from collections import Counter

def get_num_words(book_path):
    with open(book_path) as file:
        num_words = len(file.read().split())
        return num_words    
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def letters_in_book(book_path):
    with open(book_path) as file:
        text = file.read()
        lowercase_chars = [char.lower() for char in text]
        num_of_letters = Counter(lowercase_chars)
    return num_of_letters

# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

def sort_chars(num_of_letters):
    new_dict = []
    for char in num_of_letters:
        if char.isalpha():
            char = {"char": char, "count": num_of_letters[char]}
            new_dict.append(char)
           #print(f"{char['char']}: {char['count']}")
    new_dict.sort(key=lambda x: x['count'], reverse=True)
    
    return new_dict
