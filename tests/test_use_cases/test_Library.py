import pytest

from src.domain.Book import Book
from src.domain.consts import authors, genres, isbns, titles
from src.use_cases.Library import Library


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
def library(book1, book2):
    return Library([book1, book2])


@pytest.fixture
def library_with_many_books():
    books = []
    for idx in range(8):
        book = Book(titles[idx], authors[idx], 1900, genres[idx], isbns[idx])
        books.append(book)
    return Library(books)


def test_init_empty():
    lib = Library()
    assert len(lib.BookColl) == 0


def test_init_library(book1, book2):
    lib = Library([book1, book2])
    assert book1 in lib
    assert book2 in lib
    assert len(lib.IdxDict) == 2


def test_append_book(library, book3):
    library.append(book3)
    assert book3 in library
    with pytest.raises(ValueError):
        library.find_on_isbn(book3.isbn)

    library.update_index()
    assert library.find_on_isbn(book3.isbn) == book3


def test_remove_book(library, book1):
    library.remove(book1)
    assert book1 not in library
    library.update_index()
    with pytest.raises(ValueError):
        library.find_on_isbn(book1.isbn)


def test_find_on_title(library, book1):
    res = library.find_on_title('Мир')
    assert len(res) == 1
    assert res[0] == book1


def test_find_on_title_error(library):
    with pytest.raises(ValueError):
        library.find_on_title('Гарри Поттер')


def test_find_on_genre(library, book2):
    res = library.find_on_genre('Роман в стихах')
    assert len(res) == 1
    assert res[0] == book2


def test_find_on_genre_error(library):
    with pytest.raises(ValueError):
        library.find_on_genre('Детектив')


def test_find_on_author(library, book1):
    res = library.find_on_author('Толстой')
    assert len(res) == 1
    assert res[0] == book1


def test_find_on_author_error(library):
    with pytest.raises(ValueError):
        library.find_on_author('Достоевский')


def test_find_on_isbn(library, book1):
    assert library.find_on_isbn('111') == book1


def test_find_on_isbn_error(library):
    with pytest.raises(ValueError):
        library.find_on_isbn('неверный')


def test_find_on_year_int(library, book1):
    res = library.find_on_year(1869)
    assert res[0] == book1


def test_find_on_year_str(library, book1):
    res = library.find_on_year('1869')
    assert res[0] == book1


def test_find_on_year_error(library):
    with pytest.raises(ValueError):
        library.find_on_year(2035)


def test_add_library(library, book3):
    other_lib = Library([book3])
    library + other_lib
    assert book3 in library
    assert len(library.BookColl) == 3


def test_call_method(library, capsys):
    library()
    captured = capsys.readouterr()
    assert 'Книги в наличии:' in captured.out
    assert 'Война и мир' in captured.out
    assert 'Индексация книг:' in captured.out
    assert '111' in captured.out


def test_randomly_change_genre(library, capsys):
    library.randomly_change_genre()
    captured = capsys.readouterr()
    assert 'Изменил жанр книги' in captured.out


def test_run_simulation(library_with_many_books, capsys):
    library_with_many_books.run_simulation(steps=100, seed=14)
    captured = capsys.readouterr()
    assert 'Шаг номер 1:' in captured.out
    assert 'Выполнение действия' in captured.out
    assert 'Добавил книгу' in captured.out
    assert 'Невозможно удалить' in captured.out
    assert 'Удалил книгу' in captured.out
    assert 'Поиск по названию' in captured.out
    assert 'Поиск по автору' in captured.out
    assert 'Поиск по жанру' in captured.out
    assert 'Поиск по isbn' in captured.out
    assert 'Поиск по году выпуска' in captured.out
    assert 'Обновил индекс' in captured.out
    assert 'Изменил жанр' in captured.out
    assert '-' in captured.out
