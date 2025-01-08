def main():
    path = "./books/frankenstein.txt"
    report(path)

def get_book_text(path):
    with open("./books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower = text.lower()
    chars = {}
    for char in lower:
        if char.isalpha():
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    return chars

def sort_on(dict):
    return dict["count"]

def sort_chars(dict):
    chars_list = []
    for item in dict:
        chars_list.append({"char": item, "count": dict[item]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def report(path):
    text = get_book_text(path)
    num_words = get_word_count(text)
    chars_dict = get_char_count(text)
    chars_list = sort_chars(chars_dict)
    # print(sort_chars(chars_dict))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words were found in frankenstein\n")
    for char in chars_list:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")

main()
