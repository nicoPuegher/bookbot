def main():
    book_text = get_book_text("./books/frankenstein.txt")
    count_book_words(book_text)


def get_book_text(filepath):
    book_text = ""

    with open(filepath) as file:
        book_text = file.read()

    return book_text


main()
