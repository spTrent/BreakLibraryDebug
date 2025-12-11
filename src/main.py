import random

from .domain.Book import Book
from .domain.consts import authors, genres, isbns, titles, years
from .use_cases.Library import Library


def main() -> None:
    print('Hello from casino!')


if __name__ == '__main__':
    book1 = Book(
        title='1984',
        author='Джордж Оруэлл',
        year=1949,
        genre='Антиутопия',
        isbn='978-5-17-094767-7',
    )
    book2 = Book(
        title='Задача трёх тел',
        author='Лю Цысинь',
        year=2008,
        genre='Научная фантастика',
        isbn='978-5-699-85882-9',
    )
    book3 = Book(
        title='Преступление и наказание',
        author='Фёдор Достоевский',
        year=1866,
        genre='Классическая литература',
        isbn='978-5-04-116327-2',
    )
    book4 = Book(
        title='Хоббит, или Туда и обратно',
        author='Дж. Р. Р. Толкин',
        year=1937,
        genre='Фэнтези',
        isbn='978-5-17-081691-1',
    )
    book5 = Book(
        title='Мастер и Маргарита',
        author='Михаил Булгаков',
        year=1967,
        genre='Роман',
        isbn='978-5-389-01777-7',
    )
    book6 = Book(
        title='2025 год',
        author='Джордж Оруэлл',
        year=1967,
        genre='Фэнтези',
        isbn='978-5-17-094767-7',
    )

    books = [book1, book2, book3, book4, book5, book6]
    for _ in range(5):
        book = Book(
            random.choice(titles),
            random.choice(authors),
            random.choice(years),
            random.choice(genres),
            random.choice(isbns),
        )
        books.append(book)
    lib = Library(books)
    lib()
    lib.run_simulation(10)
