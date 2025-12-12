import random

from .domain.Book import Book
from .domain.consts import authors, genres, isbns, titles
from .use_cases.Library import Library
from .domain.ShelfOfBooks import ShelfOfBooks

if __name__ == '__main__':
    books = []
    for _ in range(2):
        book = Book(
            random.choice(titles),
            random.choice(authors),
            random.randint(1900, 2025),
            random.choice(genres),
            random.choice(isbns),
        )
        books.append(book)
    shelf1 = ShelfOfBooks(3, books)
    book = Book(
            random.choice(titles),
            random.choice(authors),
            random.randint(1900, 2025),
            random.choice(genres),
            random.choice(isbns),
        )
    shelf1 += book
    print(shelf1)
    