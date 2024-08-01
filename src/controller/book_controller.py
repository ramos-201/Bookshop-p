import datetime

from src.models.base import MyDatabase
from src.models.book import Book


class BookController:

    _my_database = MyDatabase

    def create(self, status, category, author, description, title):
        book = Book(
            title=title,
            status=status,
            category=category,
            author=author,
            description=description
        )
        self._my_database.add(book=book)

    def update(self, title, status, category, author, description):
        book = self._my_database.get(title=title)
        if book is not None:
            book.status = status
            book.category = category
            book.author = author
            book.description = description
            book.modified = datetime.datetime.now()
            self._my_database.update(title=title, new_book=book)
