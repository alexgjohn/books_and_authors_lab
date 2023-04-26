import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

book_repo.delete_all()
author_repo.delete_all()


author1 = Author("RF Kuang")
author2 = Author("China Mieville")
author3 = Author("Tabitha Snooz")
best_author = Author("Alex John")
author_repo.save(author1)
author_repo.save(author2)
author_repo.save(author3)
author_repo.save(best_author)

book1 = Book("Babel", "Fiction", author1)
book2 = Book("The Poppy War", "Fiction", author1)
book3 = Book("The City and The City", "Weird Fiction", author2)
book4 = Book("The Benefits of Bedtime", "Self Help", author3)
book5 = Book("Absolute Basics of Python", "Education", best_author)
book6 = Book("Trust the Process? The Skeletons in the CodeClan Closet", "Investigative Journalism", best_author)
book_repo.save(book1)
book_repo.save(book2)
book_repo.save(book3)
book_repo.save(book4)
book_repo.save(book5)
book_repo.save(book6)

