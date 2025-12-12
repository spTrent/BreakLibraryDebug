import random

from ..domain.Book import Book
from ..domain.BookCollection import BookCollection
from ..domain.consts import authors, genres, isbns, titles
from ..domain.IndexDict import IndexDict


class Library:
    def __init__(self, books: list | None = None) -> None:
        """
        Инициализирует библиотеку.

        Args:
            books: Начальный список книг. По умолчанию None.
        """
        self.BookColl = BookCollection(books)
        self.IdxDict = IndexDict.create(self.BookColl)

    def __contains__(self, item: Book) -> bool:
        """
        Проверяет наличие книги в библиотеке.

        Args:
            item: Книга для проверки.
        """
        return item in self.BookColl

    def append(self, source: 'BookCollection | Book') -> None:
        """
        Добавляет книгу или коллекцию книг в библиотеку.

        Args:
            source: Книга или коллекция для добавления.
        """
        self.BookColl += source

    def remove(self, source: 'BookCollection | Book') -> None:
        """
        Удаляет книгу или коллекцию книг из библиотеки.

        Args:
            source: Книга или коллекция для удаления.
        """
        self.BookColl -= source

    def __add__(self, source: 'Library') -> 'Library':
        """
        Объединяет две библиотеки.

        Args:
            source: Другая библиотека для объединения.

        Returns:
            Library: Текущий экземпляр библиотеки.
        """
        self.BookColl += source.BookColl
        return self

    def update_index(self) -> None:
        """Обновляет индексы на основе текущего состояния коллекции книг."""
        self.IdxDict = IndexDict.create(self.BookColl)

    def __call__(self) -> None:
        """
        Выводит информацию о состоянии библиотеки в консоль.

        Обновляет индексы и печатает список всех книг, а также содержимое
        индексов по ISBN, автору и году.
        """
        self.update_index()
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

    def find_on_title(self, item: str) -> BookCollection:
        """
        Ищет книги по названию (частичное совпадение).

        Args:
            item: Название или часть названия книги.

        Returns:
            BookCollection: Коллекция найденных книг.

        Raises:
            ValueError: Если книги с таким названием не найдены.
        """
        books = BookCollection()
        for book in self.BookColl:
            if item.lower() in book.title.lower():
                books += book

        if not books:
            raise ValueError('Нет книги с таким названием')
        return books

    def find_on_genre(self, item: str) -> BookCollection:
        """
        Ищет книги по жанру.

        Args:
            item: Название жанра.

        Returns:
            BookCollection: Коллекция найденных книг.

        Raises:
            ValueError: Если книги этого жанра не найдены.
        """
        books = BookCollection()
        for book in self.BookColl:
            if book.genre.lower() == item.lower():
                books += book

        if not books:
            raise ValueError('Нет книг этого жанра')
        return books

    def find_on_author(self, item: str) -> BookCollection:
        """
        Ищет книги по автору (частичное совпадение).

        Args:
            item: Имя автора.

        Returns:
            BookCollection: Коллекция найденных книг.

        Raises:
            ValueError: Если книги этого автора не найдены.
        """
        books = BookCollection()
        for author in self.IdxDict.author:
            if item.lower() in author.lower():
                books += BookCollection(self.IdxDict[author])

        if not books:
            raise ValueError('Нет книг этого автора')
        return books

    def find_on_isbn(self, item: str) -> Book:
        """
        Ищет книгу по ISBN.

        Args:
            item: ISBN книги.

        Returns:
            Book: Найденная книга.

        Raises:
            ValueError: Если книга с таким ISBN не найдена.
        """
        if item in self.IdxDict.isbn:
            return self.IdxDict.isbn[item][0]
        raise ValueError('Нет книги с таким ISBN')

    def find_on_year(self, item: str | int) -> BookCollection:
        """
        Ищет книги по году выпуска.

        Args:
            item: Год выпуска.

        Returns:
            BookCollection: Коллекция найденных книг.

        Raises:
            ValueError: Если книги с таким годом выпуска не найдены.
        """
        if isinstance(item, str):
            item = int(item)

        if item in self.IdxDict.year:
            return BookCollection(self.IdxDict.year[item])
        raise ValueError('Нет книг с таким годом выпуска')

    def randomly_change_genre(self) -> None:
        """
        Меняет жанр случайной книги на другой случайный жанр.
        """
        book = self.BookColl.random_pick()
        new_genre = random.choice(genres)
        book.genre = new_genre
        print(f'Изменил жанр книги "{book.title}" на "{new_genre}"')

    def run_simulation(self, steps: int = 20, seed: int | None = None) -> None:
        """
        Запускает симуляцию работы библиотеки.

        Args:
            steps: Количество шагов симуляции. По умолчанию 20.
            seed: Seed для генератора случайных чисел. По умолчанию None.
        """
        random.seed(seed)
        actions = [
            self.append,
            self.remove,
            self.find_on_title,
            self.find_on_genre,
            self.find_on_author,
            self.find_on_isbn,
            self.find_on_year,
            self.update_index,
            self.randomly_change_genre,
        ]

        for number in range(1, steps + 1):
            print(f'Шаг номер {number}:')
            pick = random.choice(actions)
            idx = random.randint(0, 7)
            book = Book(
                titles[idx], authors[idx], 1900, genres[idx], isbns[idx]
            )

            print(f'Выполнение действия {pick.__name__}')
            try:
                match pick:
                    case self.append:
                        print('Добавил книгу: ')
                        print(book)
                        self.append(book)
                    case self.remove:
                        self.remove(book)
                        print('Удалил книгу')
                        print(book)
                    case self.find_on_title:
                        print(f'Поиск по названию "{book.title}"')
                        print(self.find_on_title(book.title))
                    case self.find_on_genre:
                        print(f'Поиск по жанру "{book.genre}"')
                        print(self.find_on_genre(book.genre))
                    case self.find_on_author:
                        print(f'Поиск по автору {book.author}')
                        print(self.find_on_author(book.author))
                    case self.find_on_isbn:
                        print(f'Поиск по isbn {book.isbn}')
                        print(self.find_on_isbn(book.isbn))
                    case self.find_on_year:
                        print(f'Поиск по году выпуска {book.year}')
                        print(self.find_on_year(book.year))
                    case self.update_index:
                        print('Обновил индекс')
                        self.update_index()
                    case self.randomly_change_genre:
                        self.randomly_change_genre()
            except ValueError as msg:
                print(msg)
            print('-' * 30)
