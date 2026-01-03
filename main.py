from stats import count_characters


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    book_words = book_text.split()
    character_counts = count_characters(book_words)


def get_book_text(filepath):
    book_text = ""

    with open(filepath) as file:
        book_text = file.read()

    return book_text


main()
