import random
from typing import Generator

from .Book import Book


class BookCollection:
    def __init__(self, books: list | None = None) -> None:
        """
        Инициализирует новую коллекцию книг.

        Args:
            books: Начальный список книг. Если None, создается пустой список.
        """
        self.books = books if books is not None else []

    def __str__(self) -> str:
        """Возвращает строковое представление коллекции (список названий)."""
        return f'{[book.title for book in self.books]}'

    def __iter__(self) -> Generator:
        """Позволяет итерироваться по коллекции книг."""
        for book in self.books:
            yield book

    def __len__(self) -> int:
        """Возвращает количество книг в коллекции."""
        return len(self.books)

    def __bool__(self) -> bool:
        """Возвращает True, если коллекция не пуста."""
        return len(self.books) > 0

    def __getitem__(self, item: int | slice) -> 'Book | BookCollection':
        """
        Возвращает книгу или под-коллекцию по индексу или срезу.

        Args:
            item: Индекс или срез.

        Returns:
            Book: Если передан индекс.
            BookCollection: Если передан срез.
        """
        if isinstance(item, int):
            return self.books[item]
        return BookCollection(self.books[item])

    def __add__(self, source: 'BookCollection | Book') -> 'BookCollection':
        """
        Добавляет книгу или другую коллекцию книг.

        Args:
            source: Книга или коллекция для добавления.

        Returns:
            BookCollection: Обновленная текущая коллекция.
        """
        if isinstance(source, Book):
            self.books.append(source)
        else:
            for book in source:
                self.books.append(book)
        return self

    def __sub__(self, source: 'BookCollection | Book') -> 'BookCollection':
        """
        Удаляет книгу или коллекцию книг.

        Args:
            source: Книга или коллекция для удаления.

        Returns:
            BookCollection: Обновленная текущая коллекция.

        Raises:
            ValueError: Если удаляемой книги нет в коллекции.
        """
        if isinstance(source, Book):
            if source in self.books:
                self.books.remove(source)
            else:
                raise ValueError(
                    f'Невозможно удалить: нет книги "{source.title}"'
                )
        else:
            for book in source:
                if book not in self.books:
                    raise ValueError(
                        f'Невозможно удалить: нет книги "{book.title}"'
                    )
                self.books.remove(book)
        return self

    def random_pick(self) -> Book:
        """
        Возвращает случайную книгу из коллекции.

        Returns:
            Book: Случайно выбранный объект книги.

        Raises:
            ValueError: Если коллекция пуста.
        """
        if self.books:
            return random.choice(self.books)
        raise ValueError('Нет книг')
