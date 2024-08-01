from src.controller.book_controller import BookController


def create_new_book(status, category, author, description, title):
    BookController().create(status, category, author, description, title)


def update_book(title, status, category, author, description):
    BookController().update(title, status, category, author, description)


def delete_book(title):
    BookController().delete(title)
