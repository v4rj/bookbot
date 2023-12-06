def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    letter_count = get_char_dict(text)
    lst = get_sorted_dict(letter_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    #for loop to print out the report of how many instances of each letter there was, sorted in descending order
    for letter in lst:
        print(f"The {letter[0]} was found {letter[1]} times")

    print("\n--- End report ---")

#function to get the text to work with
def get_book_text(path):
    with open(path) as f:
        return f.read()

#function to split up the words into a list and count how many words there are    
def get_num_words(text):
    words = text.split()
    return len(words)

#function to set up a dictionary and keep track of how many times each letter was used, filtered for only alphabetic characters (a-z) in lowercase to avoid duplicates
def get_char_dict(text):
    char_dict = {}

    for key in text:
        key = key.lower()
        if key in char_dict:
            char_dict[key] += 1
        elif key.isalpha():
            char_dict[key] = 1
    
    return char_dict

#sort the dictionary into a list of tuples in descending order, based on the value of each pair
def get_sorted_dict(dict):
    dict_list = list(dict.items())
    dict_list = sorted(dict_list, key=lambda x: x[1], reverse=True)
    return dict_list

main()