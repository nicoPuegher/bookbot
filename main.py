from stats import count_characters, format_dictionary, sort_on


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    book_words = book_text.split()
    character_counts = count_characters(book_words)
    character_counts_list = format_dictionary(character_counts)
    character_counts_list.sort(reverse=True, key=sort_on)
    print_results(book_words, character_counts_list, filepath)


def get_book_text(filepath):
    book_text = ""

    with open(filepath) as file:
        book_text = file.read()

    return book_text


def print_results(book_words, character_counts_list, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {len(book_words)} total words")
    print("--------- Character Count -------")

    for dictionary in character_counts_list:
        if dictionary["char"].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")

    print("============= END ===============")


main()
