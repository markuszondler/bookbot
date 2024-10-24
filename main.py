def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list_sorted = get_chars_dict_sorted_num(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char in chars_list_sorted:
        if not char["char"].isalpha():
            continue
        c = char["char"]
        n = char["num"]
        print(f"The '{c}' character was found {n} times")

    print("--- End report ---")


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


def sort_on_key_num(dict):
    return dict["num"]


def get_chars_dict_sorted_num(dict):
    tmp_list = []
    for char in dict:
        tmp_list.append({"char": char, "num": dict[char]})
    tmp_list.sort(reverse=True, key=sort_on_key_num)
    return tmp_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
