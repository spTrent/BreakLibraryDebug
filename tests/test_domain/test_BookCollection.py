import pytest

from src.domain.Book import Book
from src.domain.BookCollection import BookCollection


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


def test_init_empty():
    coll = BookCollection()
    assert len(coll) == 0
    assert coll.books == []


def test_init_with_list(book1):
    coll = BookCollection([book1])
    assert len(coll) == 1
    assert coll.books[0] == book1


def test_str(collection):
    res = str(collection)
    assert 'Война и мир' in res
    assert 'Евгений Онегин' in res


def test_iter(collection, book1, book2):
    books = [book for book in collection]
    assert len(books) == 2
    assert books[0] == book1
    assert books[1] == book2


def test_len(collection):
    assert len(collection) == 2


def test_bool(collection):
    assert bool(collection) is True
    assert bool(BookCollection()) is False


def test_getitem_index(collection, book1):
    assert collection[0] == book1
    assert isinstance(collection[0], Book)


def test_getitem_slice(collection, book1):
    sub = collection[:1]
    assert isinstance(sub, BookCollection)
    assert len(sub) == 1
    assert sub[0] == book1


def test_add_book(collection, book3):
    collection += book3
    assert len(collection) == 3
    assert collection[2] == book3


def test_add_collection(collection, book3):
    other = BookCollection([book3])
    collection += other
    assert len(collection) == 3
    assert collection[2] == book3


def test_sub_book(collection, book1):
    collection -= book1
    assert len(collection) == 1
    assert book1 not in collection


def test_sub_collection(collection, book1, book2):
    other = BookCollection([book1])
    collection -= other
    assert len(collection) == 1
    assert collection[0] == book2


def test_sub_book_error(collection, book3):
    with pytest.raises(ValueError):
        collection -= book3


def test_sub_collection_error(collection, book3):
    other = BookCollection([book3])
    with pytest.raises(ValueError):
        collection -= other


def test_random_pick(collection):
    book = collection.random_pick()
    assert book in collection


def test_random_pick_error():
    coll = BookCollection()
    with pytest.raises(ValueError):
        coll.random_pick()
