from flask import Flask, render_template, Blueprint, request, redirect
books_blueprint = Blueprint("books", __name__)
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo
from models.book import Book

@books_blueprint.route('/books')
def books():
    books = book_repo.select_all()
    return render_template('books/index.jinja', books_in_list = books)

@books_blueprint.route('/books/new')
def new_book():
    authors = author_repo.select_all()
    return render_template('books/new.jinja', authors_on_file = authors)

@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repo.select(id)
    return render_template('books/show.jinja', book = book)