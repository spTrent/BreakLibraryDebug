from typing import Any


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: str | int,
        genre: str,
        isbn: str,
        cost: int = 100,
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
        self.cost = cost

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Book):
            return False
        return (
            self.title == other.title
            and self.author == other.author
            and self.genre == other.genre
            and self.isbn == other.isbn
        )

    def __str__(self) -> str:
        return f"""Книга: "{self.title}".
Автор: {self.author}.
Год Выпуска: {self.year}.
Жанр: {self.genre}.
ISBN: {self.isbn}.
Стоимость аренды: {self.cost}"""
