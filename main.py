def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"--- Begin report for {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print(get_char_count(text))


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_char_count(text):
    chars = []
    lower_text = text.lower()

def sort_on(dict):
    return dict("num")

main()
