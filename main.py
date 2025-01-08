def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    chars_dict = get_char_count(text)
    print(f"{num_words} words were found in frankenstein")
    print(chars_dict)

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
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars
main()
