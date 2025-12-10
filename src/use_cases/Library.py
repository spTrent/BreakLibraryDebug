from ..domain.Book import Book
from ..domain.BookCollection import BookCollection
from ..domain.IndexDict import IndexDict


class Library:
    def __init__(self, books: list | None = None) -> None:
        if books is None:
            books = []
        self.BookColl = BookCollection(books)
        self.IdxDict = IndexDict.create(self.BookColl)

    def __contains__(self, item: Book) -> bool:
        return item in self.BookColl

    def append(self, source: 'BookCollection | Book') -> None:
        self.BookColl += source
        self.IdxDict = IndexDict.create(self.BookColl)

    def remove(self, source: 'BookCollection | Book') -> None:
        self.BookColl -= source
        self.IdxDict = IndexDict.create(self.BookColl)

    def __add__(self, source: 'Library') -> 'Library':
        self.BookColl += source.BookColl
        self.IdxDict += source.IdxDict
        return self

    def __call__(self) -> None:
        print('Книги в наличии: ')
        for number, book in enumerate(self.BookColl, start=1):
            print(f'{number}. "{book.title}"')

        print('Индексация книг:\n\tПо isbn:')
        for isbn in self.IdxDict:
            print(f'\t\t{isbn}:', end=' ')
            for book in self.IdxDict[isbn]:
                print(f'"{book.title}"', end=', ')
            print()

        print('\tПо автору:')
        for author in self.IdxDict.author:
            print(f'\t\t{author}:', end=' ')
            for book in self.IdxDict.author[author]:
                print(f'"{book.title}"', end=', ')
            print()

        print('\tПо году выпуска:')
        for year in self.IdxDict.year:
            print(f'\t\t{year}:', end=' ')
            for book in self.IdxDict.year[year]:
                print(f'"{book.title}"', end=', ')
            print()


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
lib = Library(books)
lib()
