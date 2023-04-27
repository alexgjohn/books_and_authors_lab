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


@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repo.select(id)
    return render_template('books/show.jinja', book = book)

@books_blueprint.route('/books/<id>/delete', methods = ['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')

@books_blueprint.route('/books/<id>/edit')
def edit_book(id):
    book = book_repo.select(id)
    authors = author_repo.select_all()
    return render_template('/books/edit.jinja', book_on_file=book, authors_on_file=authors)

@books_blueprint.route('/books/<id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, genre, author, id)
    book_repo.update(book)
    return redirect('/books')

#works but doesn't display author name
@books_blueprint.route('/books/author/<id>')
def show_books_by_author(id):
    author = author_repo.select(id)
    books_by_author = book_repo.books_by_author(author)
    return render_template('books/index.jinja', books_in_list = books_by_author)




