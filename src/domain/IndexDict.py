from collections import defaultdict
from typing import Generator

from .Book import Book
from .BookCollection import BookCollection


class IndexDict:
    def __init__(self, isbn: dict, author: dict, year: dict) -> None:
        self.isbn = isbn
        self.author = author
        self.year = year

    @staticmethod
    def create(source: 'BookCollection | None' = None) -> 'IndexDict':
        isbn = defaultdict(list)
        author = defaultdict(list)
        year = defaultdict(list)
        if source is not None:
            for book in source:
                isbn[book.isbn].append(book)
                author[book.author].append(book)
                year[book.year].append(book)
            idxDict = IndexDict(isbn, author, year)
        return idxDict

    def __iter__(self) -> Generator:
        for isbn in self.isbn:
            yield isbn

    def __len__(self) -> int:
        return len(self.isbn)

    def __getitem__(self, source: str) -> list:
        res = self.isbn.get(source, None)
        if res is not None:
            return res
        res = self.author.get(source, None)
        if res is not None:
            return res
        res = self.year.get(source, None)
        if res is not None:
            return res
        raise ValueError('Нет такого ключа')

    def __add__(self, source: 'IndexDict | Book') -> 'IndexDict':
        if isinstance(source, Book):
            self.isbn[source.isbn].append(source)
            self.author[source.author].append(source)
            self.year[source.year].append(source)
        else:
            for isbn in source:
                for book in source[isbn]:
                    self.isbn[book.isbn].append(book)
                    self.author[book.author].append(book)
                    self.year[book.year].append(book)
        return IndexDict(self.isbn, self.author, self.year)

    def __sub__(self, source: 'IndexDict | Book') -> 'IndexDict':
        if isinstance(source, Book):
            self.isbn[source.isbn].remove(source)
            self.author[source.author].remove(source)
            self.year[source.year].remove(source)
        else:
            for book in source:
                self.isbn[book.isbn].remove(book)
                self.author[book.author].remove(book)
                self.year[book.year].remove(book)
        return IndexDict(self.isbn, self.author, self.year)
