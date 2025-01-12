from string import ascii_lowercase 

def get_word_count(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    chars = {}
    for c in book_text.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_on_value(t):
    return t[1] # sort on value of tuple

def get_book_stats(book_name, book_text):
    word_count = get_word_count(book_text)
    chars = get_char_count(book_text)
    header = f"--- Begin report of {book_name} ---\n"
    footer = f"--- End report ---\n"
    body = f"{word_count} words found in the document\n\n"
    vals = []
    for c in ascii_lowercase:
        if c in chars:
           vals.append((c, chars[c]))
    vals.sort(key=sort_on_value, reverse=True)
    for n, l in vals:
        body += f"The '{l} character was found {n} times\n"
    return header + body + footer

if __name__ == '__main__':
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(get_book_stats(path_to_file, file_contents))

