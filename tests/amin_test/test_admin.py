from src.admin.admin_option import create_new_book
from src.models.base import MyDatabase


def test_create_book_success():
    data = {
        'status': 'avaliable',
        'category': 'fiction',
        'author': 'name_test',
        'description': 'description_test',
        'title': 'title_test'
    }
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
