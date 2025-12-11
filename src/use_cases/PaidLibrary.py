from ..domain.Book import Book
from ..domain.BookCollection import BookCollection
from .Library import Library


class PaidLibrary(Library):
    def __init__(self, balance: int = 1000, books: list | None = None) -> None:
        """
        Инициализирует платную библиотеку.

        Args:
            balance: Начальный баланс. По умолчанию 1000.
            books: Начальный список книг. По умолчанию None.
        """
        super().__init__(books)
        self.balance = balance

    def append(self, source: 'BookCollection | Book') -> None:
        """
        Покупает книгу или коллекцию книг.

        Args:
            source: Книга или коллекция для покупки.
        """
        new_balance = self.balance

        if isinstance(source, Book):
            new_balance -= source.cost
        else:
            for book in source:
                new_balance -= book.cost

        if new_balance >= 0:
            super().append(source)
            self.balance = new_balance
        else:
            print('Недостаточно средств для покупки')

    def remove(self, source: 'BookCollection | Book') -> None:
        """
        Продает (удаляет) книгу или коллекцию книг.

        Args:
            source: Книга или коллекция для продажи.
        """
        if isinstance(source, Book):
            self.balance += source.cost
        else:
            for book in source:
                self.balance += book.cost

        super().remove(source)

    def __add__(self, source: 'Library | PaidLibrary') -> 'PaidLibrary':
        """
        Объединяет две библиотеки.

        Args:
            source: Библиотека для объединения.

        Returns:
            PaidLibrary: Текущий экземпляр с обновленными книгами и балансом.
        """
        super().__add__(source)

        if isinstance(source, PaidLibrary):
            self.balance += source.balance

        return self
