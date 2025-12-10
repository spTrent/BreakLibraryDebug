from ..domain.Book import Book
from ..domain.BookCollection import BookCollection
from .Library import Library


class PaidLibrary(Library):
    def __init__(self, balance: int | None, books: list | None = None) -> None:
        super().__init__(books)
        self.balance = balance if balance is not None else 1000

    def append(self, source: 'BookCollection | Book') -> None:
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
        if isinstance(source, Book):
            self.balance += source.cost
        else:
            for book in source:
                self.balance += book.cost
        super().remove(source)

    def __add__(self, source: 'Library | PaidLibrary') -> 'PaidLibrary':
        super().__add__(source)
        if isinstance(source, PaidLibrary):
            self.balance += source.balance
        return self
