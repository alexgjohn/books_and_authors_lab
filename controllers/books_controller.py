from flask import Flask, render_template, Blueprint, request, redirect
books_blueprint = Blueprint("books", __name__)
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo
from models.book import Book

@books_blueprint.route('/books')
def books():
    books = book_repo.select_all()
    return render_template('books/index.jinja', books_in_list = books)

@books_blueprint.route('/books/new', methods = ['GET'])
def new_book():
    authors = author_repo.select_all()
    return render_template('books/new.jinja', authors_on_file = authors)


@books_blueprint.route('/books', methods = ['POST'])
def add_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, genre, author)
    book_repo.save(book)
    return redirect('/books')


# @tasks_blueprint.route("/tasks",  methods=['POST'])
# def create_task():
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed)
#     task_repository.save(task)
#     return redirect('/tasks')

@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repo.select(id)
    return render_template('books/show.jinja', book = book)

@books_blueprint.route('/books/<id>/delete', methods = ['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')


