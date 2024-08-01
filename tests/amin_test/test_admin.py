import pytest

from src.admin_option import create_new_book, update_book, delete_book
from src.models.base import MyDatabase
from src.models.book import Book

data = {
    'status': 'available',
    'category': 'fiction',
    'author': 'name_test',
    'description': 'description_test',
    'title': 'title_test'
}


# TODO: tests, poder obtener los libros y hacer los cambios por id unico.

@pytest.fixture
def setup_my_database():
    MyDatabase.books.clear()
    yield


@pytest.fixture
def book_created(setup_my_database):
    book = Book(
        status=data['status'],
        category=data['category'],
        author=data['author'],
        description=data['description'],
        title=data['title']
    )
    MyDatabase.add(book=book)


def test_create_book_success():
    create_new_book(
        status=data['status'],
        category= data['category'],
        author=data['author'],
        description=data['description'],
        title=data['title']
    )
    book_created = MyDatabase.get(title=data['title'])
    assert book_created.status == data['status']
    assert book_created.category == data['category']
    assert book_created.author == data['author']
    assert book_created.description == data['description']
    assert book_created.title == data['title']


def test_update_data_book_success(book_created):
    new_data = {
        'status': 'not available',
        'category': 'romantic',
        'author': 'name_updated_test',
        'description': 'description_updated_test',
    }
    update_book(
        title=data['title'],  status=new_data['status'], category=new_data['category'],
        author=new_data['author'], description=new_data['description']
    )
    book_updated = MyDatabase.get(title=data['title'])
    assert book_updated.status == new_data['status']
    assert book_updated.category == new_data['category']
    assert book_updated.author == new_data['author']
    assert book_updated.description == new_data['description']
    assert book_updated.title == data['title']

# TODO: tests,  si no existe un titulo, si solo quiere actualizar un campo.


def test_delete_book_success(book_created):
    delete_book(title=data['title'])
    deleted_book = MyDatabase.get(title=data['title'])
    assert deleted_book is None
