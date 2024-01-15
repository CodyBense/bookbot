def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    #print(num_of_letter(text))
    dict_to_list(num_of_letter(text))
    print("\n--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def num_of_letter(text):
    count = {}
    for letter in text.lower():
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    return count


def dict_to_list(dict):
    dict_list = list(dict.items())
    dict_list.sort()
    for item in dict_list:
        if item[0].isalpha():
            print(f"The '{item[0]}' character is found {item[1]} times")


main()
