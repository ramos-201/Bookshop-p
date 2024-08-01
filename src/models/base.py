class MyDatabase:
    books = []

    @classmethod
    def add(cls, book):
        cls.books.append(book)

    @classmethod
    def get(cls, title):
        for book in cls.books:
            if book.title == title:
                return book
        return None
