from .Book import Book
from .BookCollection import BookCollection


class ShelfOfBooks(BookCollection):
    def __init__(self, max_len: int, books: list | None = None) -> None:
        super().__init__(books)
        self.max_len = max_len

    @staticmethod
    def create(max_len: int, books: list | None = None) -> 'ShelfOfBooks':
        if books is None:
            books = []
        if len(books) > max_len:
            raise ValueError(
                f"""Слишком много книг ({len(books)}).
                Вместимость полки - {max_len}"""
            )
        if max_len <= 0:
            raise ValueError(f'Размер полки не может быть {max_len}')
        shelf = ShelfOfBooks(max_len, books)
        return shelf

    def __add__(self, source: 'Book | BookCollection') -> 'ShelfOfBooks':
        if isinstance(source, Book) and len(self) + 1 <= self.max_len:
            super().__add__(source)
            return self
        elif isinstance(source, Book):
            print('Невозможно добавить, потому что полка полностью заполнена')
            return self
        elif (
            isinstance(source, BookCollection)
            and len(source) + len(self) < self.max_len
        ):
            super().__add__(source)
            return self
        else:
            print(
                'Невозможно добавить'
                'потому что полка будет полностью переполнена'
            )
            return self
