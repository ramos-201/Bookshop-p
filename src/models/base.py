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

    @classmethod
    def update(cls, title, new_book):
        for k, book in enumerate(cls.books):
            if book.title == title:
                cls.books[k] = new_book

    @classmethod
    def delete(cls, title):
        for k, book in enumerate(cls.books):
            if book.title == title:
                cls.books.pop(k)
