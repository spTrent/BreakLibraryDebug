class Book:
    def __init__(
        self, title: str, author: str, year: str | int, genre: str, isbn: str
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __str__(self) -> str:
        return f"""Книга: "{self.title}".
Автор: {self.author}.
Год Выпуска: {self.year}.
Жанр: {self.genre}.
ISBN: {self.isbn}."""


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
