import random

from .domain.Book import Book
from .domain.consts import authors, genres, isbns, titles
from .use_cases.Library import Library

if __name__ == '__main__':
    # books = [Book('Мёртвые души', 'Николай Гоголь', 1842, 'Поэма', '333')]
    # for _ in range(5):
    #     book = Book(
    #         random.choice(titles),
    #         random.choice(authors),
    #         random.randint(1900, 2025),
    #         random.choice(genres),
    #         random.choice(isbns),
    #     )
    #     books.append(book)
    # lib = Library()
    # lib()
    # lib.run_simulation(10, seed=20)

    lib1 = Library()
    lib1.append(Book('Мёртвые души', 'Николай Гоголь', 1842, 'Поэма', '333'))
    lib2 = Library()
    print(len(lib2.BookColl))
    lib1 += lib2
    lib1()
    