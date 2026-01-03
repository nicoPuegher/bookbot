def count_characters(book_words):
    character_counts = {}

    for word in book_words:
        for char in word:
            lowercase_char = char.lower()

            if lowercase_char not in character_counts:
                character_counts[lowercase_char] = 1
            else:
                character_counts[lowercase_char] += 1

    return character_counts


def format_dictionary(character_counts):
    character_counts_list = []

    for character in character_counts:
        character_counts_list.append(
            {"char": character, "num": character_counts[character]}
        )

    return character_counts_list


def sort_on(items):
    return items["num"]
