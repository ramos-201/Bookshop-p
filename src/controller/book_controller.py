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
