from flask import Flask, send_file, request, redirect, render_template, make_response, Response
from app import app, db
from models import User, Author, Genre, Book
import json

user = ""

@app.route('/')
def index():
    return send_file('templates/index.html')


@app.route('/user', methods=['GET'])
def get_user():
    if user == "":
        response = Response(response=user, status=200, mimetype='application/json')
        return response
    else:
        response = Response(response=User.to_json(user), status=200, mimetype='application/json')
        return response


@app.route('/login', methods=['POST'])
def login():
    users = User.query.all()
    login_user = request.json
    for u in users:
        if u.username == login_user['username'] and u.password == login_user['password']:
            global user
            user = u
            break

    if (not user):
        response = Response(status=401)
        return response
    else:
        response = Response(response=User.to_json(user), status=200, mimetype='application/json')
        return response


@app.route('/logout', methods=['POST'])
def logout():
    global user
    user = ""
    response = Response(status=200)
    return response


@app.route('/userSettings', methods=['POST'])
def user_settings():
    global user
    requestUser = request.json
    modifiedUser = User.query.filter(User.id == user.id).one()
    if modifiedUser.password == requestUser['currentPassword']:
        if requestUser['newPassword'] != requestUser['confirmNewPassword']:
            response = Response(status=409)
            return response
        modifiedUser.name = requestUser['name']
        modifiedUser.password = requestUser['newPassword']
        user = modifiedUser
        print(User.to_json(user))
        db.session.commit()
        response = Response(status=200)
        return response
    else:
        response = Response(status=401)
        return response


@app.route('/addAuthor', methods=['POST'])
def add_author():
    authors = Author.query.all()
    author = request.json
    for a in authors:
        if a.name == author['name']:
            response = Response(status=409)
            return response
    new_author = Author(name=author['name'])
    db.session.add(new_author)
    db.session.commit()
    response = Response(status=200)
    return response


@app.route('/authors', methods=['GET'])
def get_authors():
    author_result = Author.query.all()
    authors = [author.to_dict() for author in author_result]
    response = Response(response=json.dumps(authors), status=200, mimetype='application/json')
    return response


@app.route('/genres', methods=['GET'])
def get_genres():
    genre_result = Genre.query.all()
    genres = [genre.to_dict() for genre in genre_result]
    response = Response(response=json.dumps(genres), status=200, mimetype='application/json')
    return response


@app.route('/addBook', methods=['POST'])
def add_book():
    books = Book.query.all()
    book = request.json
    for b in books:
        if b.author == book['author']['name'] and b.title == book['title']:
            response = Response(status=409)
            return response

    new_book = Book(author=book['author']['name'], title=book['title'], genre=book['genre']['genre'], quantity=0, available=0)
    db.session.add(new_book)
    db.session.commit()
    response = Response(status=200)
    return response


if __name__ == '__main__':
    app.run()