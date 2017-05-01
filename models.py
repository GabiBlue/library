import json

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

    def to_dict(self):
        fields = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_dict(self):
        fields = {
            'id': self.id,
            'name': self.name,
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    quantity = db.Column(db.Integer)
    available = db.Column(db.Integer)

    def to_dict(self):
        fields = {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'genre': self.genre,
            'quantity': self.quantity,
            'available': self.available
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    user = db.Column(db.String)

    def to_dict(self):
        fields = {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'user': self.user
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

    def to_dict(self):
        fields = {
            'id': self.id,
            'genre': self.genre
        }
        return fields

    def to_json(self):
        return json.dumps(self.to_dict())