import pytest

from src.domain.Book import Book
from src.domain.BookCollection import BookCollection
from src.domain.ShelfOfBooks import ShelfOfBooks


@pytest.fixture
def book1():
    return Book('Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', '111')


@pytest.fixture
def book2():
    return Book(
        'Евгений Онегин', 'Александр Пушкин', 1833, 'Роман в стихах', '222'
    )


@pytest.fixture
def book3():
    return Book('Мёртвые души', 'Николай Гоголь', 1842, 'Поэма', '333')


def test_create_valid(book1):
    shelf = ShelfOfBooks.create(max_len=5, books=[book1])
    assert len(shelf) == 1
    assert shelf.max_len == 5
    assert shelf[0] == book1


def test_create_empty_valid():
    shelf = ShelfOfBooks.create(max_len=3)
    assert len(shelf) == 0
    assert shelf.max_len == 3


def test_create_invalid_size():
    with pytest.raises(ValueError, match='Размер полки не может быть -1'):
        ShelfOfBooks.create(max_len=-1)

    with pytest.raises(ValueError, match='Размер полки не может быть 0'):
        ShelfOfBooks.create(max_len=0)


def test_create_overflow_initial(book1, book2):
    with pytest.raises(ValueError, match='Слишком много книг'):
        ShelfOfBooks.create(max_len=1, books=[book1, book2])


def test_add_book_success(book1, book2):
    shelf = ShelfOfBooks.create(max_len=2, books=[book1])
    shelf += book2
    assert len(shelf) == 2
    assert shelf[1] == book2


def test_add_book_overflow(book1, book2, capsys):
    shelf = ShelfOfBooks.create(max_len=1, books=[book1])
    shelf += book2
    assert len(shelf) == 1
    assert book2 not in shelf

    captured = capsys.readouterr()
    assert 'Невозможно добавить' in captured.out
    assert 'полка полностью заполнена' in captured.out


def test_add_collection_success(book1, book2, book3):
    shelf = ShelfOfBooks.create(max_len=5, books=[book1])
    to_add = BookCollection([book2, book3])
    shelf += to_add

    assert len(shelf) == 3
    assert shelf[1] == book2
    assert shelf[2] == book3


def test_add_collection_overflow(book1, book2, book3, capsys):
    shelf = ShelfOfBooks.create(max_len=2, books=[book1])
    to_add = BookCollection([book2, book3])
    shelf += to_add
    assert len(shelf) == 1

    captured = capsys.readouterr()
    assert 'Невозможно добавить' in captured.out
    assert 'полка будет переполнена' in captured.out
