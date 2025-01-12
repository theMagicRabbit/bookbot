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

if __name__ == '__main__':
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(get_word_count(file_contents))
    print(get_char_count(file_contents))

