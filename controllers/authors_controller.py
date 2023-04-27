from flask import Flask, render_template, Blueprint, request, redirect
authors_blueprint = Blueprint("authors", __name__)
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo
from models.author import Author
from models.book import Book

@authors_blueprint.route('/authors')
def authors():
    authors = author_repo.select_all()
    return render_template('authors/index.jinja', authors_list = authors)

@authors_blueprint.route('/authors/new')
def new_author():
    return render_template('/authors/new.jinja')
