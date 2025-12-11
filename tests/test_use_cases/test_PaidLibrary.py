import pytest

from src.domain.Book import Book
from src.domain.BookCollection import BookCollection
from src.use_cases.Library import Library
from src.use_cases.PaidLibrary import PaidLibrary


@pytest.fixture
def book_expensive():
    book = Book('Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', '111', 500)
    return book


@pytest.fixture
def book():
    book = Book('Cheap Book', 'Author B', 2000, 'Genre', '222')
    return book


@pytest.fixture
def paid_library():
    return PaidLibrary(balance=1000)


def test_init_paid_library():
    lib = PaidLibrary(balance=500)
    assert lib.balance == 500
    assert len(lib.BookColl) == 0


def test_append_book_success(paid_library, book):
    initial_balance = paid_library.balance
    paid_library.append(book)

    assert book in paid_library
    assert paid_library.balance == initial_balance - book.cost


def test_append_book_fail(paid_library, book_expensive, capsys):
    paid_library.balance = 100
    paid_library.append(book_expensive)

    assert book not in paid_library
    assert paid_library.balance == 100
    captured = capsys.readouterr()
    assert 'Недостаточно средств' in captured.out


def test_append_collection_success(paid_library, book, book_expensive):
    coll = BookCollection([book, book_expensive])
    init_balance = paid_library.balance
    paid_library.append(coll)

    assert book in paid_library
    assert book_expensive in paid_library
    assert (
        paid_library.balance == init_balance - book.cost - book_expensive.cost
    )


def test_remove_book_sells(paid_library, book):
    paid_library.append(book)
    assert paid_library.balance == 900
    paid_library.remove(book)
    assert book not in paid_library
    assert paid_library.balance == 1000


def test_remove_collection(paid_library, book):
    collection = BookCollection([book])
    init_balance = paid_library.balance
    paid_library.append(book)
    paid_library.remove(collection)
    assert book not in paid_library
    assert paid_library.balance == init_balance


def test_add_libraries(paid_library, book):
    other_lib = PaidLibrary(balance=500)
    other_lib.BookColl += book
    paid_library + other_lib
    assert paid_library.balance == 1000 + 500
    assert book in paid_library


def test_add_simple_library(paid_library, book):
    simple_lib = Library([book])

    paid_library + simple_lib

    assert paid_library.balance == 1000
    assert book in paid_library
