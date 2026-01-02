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
