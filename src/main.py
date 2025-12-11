import random

from .domain.Book import Book
from .domain.consts import authors, genres, isbns, titles
from .use_cases.Library import Library

if __name__ == '__main__':
    books = []
    for _ in range(5):
        book = Book(
            random.choice(titles),
            random.choice(authors),
            random.randint(1900, 2025),
            random.choice(genres),
            random.choice(isbns),
        )
        books.append(book)
    lib = Library(books)
    lib()
    lib.run_simulation(10)
