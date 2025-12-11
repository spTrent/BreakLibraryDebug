import pytest

from src.domain.Book import Book


@pytest.fixture
def book():
    return Book(
        'Война и Мир',
        'Война и мир',
        'Лев Толстой',
        1869,
        'Роман-эпопея',
        '978-5-389-06256-6',
    )


@pytest.fixture
def bookcopy():
    return Book(
        'Война и Мир',
        'Война и мир',
        'Лев Толстой',
        1869,
        'Роман-эпопея',
        '978-5-389-06256-6',
    )


def test_book_str(book, capsys):
    print(book)
    captured = capsys.readouterr()
    assert 'Война и Мир' in captured.out
    assert 'Роман-эпопея' in captured.out


def test_books_equal(book, bookcopy):
    assert book == bookcopy


def test_book_not_equal_list(book):
    assert not (book == [])
