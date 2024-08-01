import datetime
import uuid


class Book:

    def __init__(self, title, status, category, author, description):
        self._id = uuid.uuid4()
        self._title = title
        self._created = datetime.datetime.now()
        self._modified = datetime.datetime.now()
        self._status = status
        self._category = category
        self._author = author
        self._description = description

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    @property
    def id(self):
        return self._id

    @property
    def created(self):
        return self._created

    @property
    def modified(self):
        return self._modified

    @property
    def category(self):
        return self._category

    @property
    def author(self):
        return self._author

    @property
    def description(self):
        return self._description

    @modified.setter
    def modified(self, value):
        self._modified = value

    @status.setter
    def status(self, value):
        self._status = value

    @category.setter
    def category(self, value):
        self._category = value

    @author.setter
    def author(self, value):
        self._author = value

    @description.setter
    def description(self, value):
        self._description = value
