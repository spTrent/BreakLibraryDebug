import pytest

from src.domain.Book import Book
from src.domain.BookCollection import BookCollection
from src.domain.IndexDict import IndexDict


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


@pytest.fixture
def collection(book1, book2):
    return BookCollection([book1, book2])


@pytest.fixture
def index_dict(collection):
    return IndexDict.create(collection)


def test_create_empty():
    idx = IndexDict.create(None)
    assert len(idx) == 0
    assert idx.isbn == {}


def test_create_from_collection(index_dict, book1, book2):
    assert len(index_dict) == 2
    assert book1 in index_dict.author['Лев Толстой']
    assert book2 in index_dict.author['Александр Пушкин']


def test_getitem_isbn(index_dict, book1):
    res = index_dict[book1.isbn]
    assert isinstance(res, list)
    assert res[0] == book1


def test_getitem_author(index_dict, book2):
    res = index_dict['Александр Пушкин']
    assert res[0] == book2


def test_getitem_year(index_dict, book1):
    res = index_dict[1869]
    assert res[0] == book1


def test_getitem_error(index_dict):
    with pytest.raises(ValueError):
        index_dict['Несуществующий ключ']


def test_iter(index_dict, book1, book2):
    keys = [key for key in index_dict]
    assert len(keys) == 2
    assert book1.isbn in keys
    assert book2.isbn in keys


def test_add_book(index_dict, book3):
    index_dict += book3
    assert len(index_dict) == 3
    assert book3 in index_dict['Николай Гоголь']


def test_add_index_dict(index_dict, book3):
    other_coll = BookCollection([book3])
    other_idx = IndexDict.create(other_coll)
    index_dict += other_idx
    assert len(index_dict) == 3
    assert index_dict['Николай Гоголь'][0] == book3


def test_sub_book(index_dict, book1):
    index_dict -= book1
    assert book1 not in index_dict.author['Лев Толстой']


def test_sub_collection(index_dict, book1):
    books_to_remove = [book1]
    index_dict -= books_to_remove
    assert book1 not in index_dict.author['Лев Толстой']


def test_sub_book_error(index_dict, book3):
    with pytest.raises(ValueError):
        index_dict -= book3
