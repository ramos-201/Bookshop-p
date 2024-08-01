from src.controller.book_controller import BookController


def create_new_book(status, category, author, description, title):
    BookController().create(status, category, author, description, title)
