import random
from typing import Generator

from .Book import Book


class BookCollection:
    def __init__(self, books: list | None = None) -> None:
        self.books = books if books is not None else []

    def __str__(self) -> str:
        return f'{[book.title for book in self.books]}'

    def __iter__(self) -> Generator:
        for book in self.books:
            yield book

    def __len__(self) -> int:
        return len(self.books)

    def __bool__(self) -> bool:
        return len(self.books) > 0

    def __getitem__(self, item: int | slice) -> 'Book | BookCollection':
        if isinstance(item, Book):
            return self.books[item]
        return BookCollection(self.books[item])

    def __add__(self, source: 'BookCollection | Book') -> 'BookCollection':
        if isinstance(source, Book):
            self.books.append(source)
        else:
            for book in source:
                self.books.append(book)
        return BookCollection(self.books)

    def __sub__(self, source: 'BookCollection | Book') -> 'BookCollection':
        if isinstance(source, Book) and Book in self.books:
            self.books.remove(source)
        elif isinstance(source, Book):
            raise ValueError(f'Невозможно удалить: нет книги "{source.title}"')
        else:
            for book in source:
                if book not in self.books:
                    raise ValueError(
                        f'Невозможно удалить: нет книги "{book.title}"'
                    )
                self.books.remove(book)
        return BookCollection(self.books)

    def random_pick(self) -> Book:
        if self.books:
            return random.choice(self.books)
        raise ValueError('Нет книг')
