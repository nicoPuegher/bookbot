# 📚 BookBot

![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-complete-green)

BookBot is a simple command-line program written in Python.

It takes a text file as input and prints basic statistics about the book, like word count and character frequency.

## What it does

Given a text file, BookBot:

1. Reads the full book
2. Counts how many words it has
3. Counts how many times each character appears
4. Prints the results in the terminal

Only alphabetical characters are included in the character count.

## Requirements

- Python 3.x
- A text file to analyze (for example, a .txt book)

No external libraries needed.

## How to use it

1. Clone the repository:

```shell
    git clone https://github.com/nicoPuegher/bookbot.git
    cd bookbot
```

2. Run the program with a path to a book:

```shell
    python3 main.py path/to/book.txt
```

Example:

```shell
    python3 main.py books/frankenstein.txt
````

## Example output

```diff
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found 77986 total words
    --------- Character Count -------
    a: 46043
    b: 9021
    c: 11532
    ...
    ============= END ===============
```

## Project structure

```graphql
    .
    ├── main.py     # Program entry point
    ├── stats.py    # Text analysis functions
    └── books/      # (Optional) folder for book files
```

## Notes

- The program expects one argument: the path to the book file.
- If no file is provided, it will show usage instructions and exit.
