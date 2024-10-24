def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in document {book_path}")
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars_dict = {}
    for c in text:
        lower = c.lower()
        if lower in chars_dict:
            chars_dict[lower] += 1
        else:
            chars_dict[lower] = 1
    return chars_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
