from .Book import Book
from .BookCollection import BookCollection


class ShelfOfBooks(BookCollection):
    def __init__(self, max_len: int, books: list | None = None) -> None:
        """
        Инициализирует полку.

        Args:
            max_len: Вместимость полки.
            books: Начальный список книг. По умолчанию None.
        """
        super().__init__(books)
        self.max_len = max_len

    @staticmethod
    def create(max_len: int, books: list | None = None) -> 'ShelfOfBooks':
        """
        Метод для создания полки.

        Args:
            max_len: Максимальная вместимость полки (должна быть > 0).
            books: Список книг для добавления.

        Returns:
            ShelfOfBooks: Созданный объект полки.

        Raises:
            ValueError: Если max_len <= 0 или
            количество книг превышает max_len.
        """
        if max_len <= 0:
            raise ValueError(f'Размер полки не может быть {max_len}')

        if books is None:
            books = []

        if len(books) > max_len:
            raise ValueError(
                f"""Слишком много книг ({len(books)}).
                Вместимость полки - {max_len}"""
            )

        shelf = ShelfOfBooks(max_len, books)
        return shelf

    def __add__(self, source: 'Book | BookCollection') -> 'ShelfOfBooks':
        """
        Добавляет книгу или коллекцию книг с проверкой вместимости.

        Args:
            source: Книга или коллекция для добавления.

        Returns:
            ShelfOfBooks: Текущий объект полки.
        """
        if isinstance(source, Book) and len(self) + 1 <= self.max_len:
            super().__add__(source)
        elif isinstance(source, Book):
            print('Невозможно добавить, потому что полка полностью заполнена')
        elif (
            isinstance(source, BookCollection)
            and len(source) + len(self) <= self.max_len
        ):
            super().__add__(source)
        else:
            print('Невозможно добавитьпотому что полка будет переполнена')
        return self
