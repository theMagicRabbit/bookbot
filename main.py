def get_word_count(book_text):
    return len(book_text.split())

if __name__ == '__main__':
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    print(get_word_count(file_contents))

