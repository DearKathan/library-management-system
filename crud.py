from models import Book, Member, Transactions
from database import session

def add_book(title, author, isbn, count):
    print("Adding book to the database..")
    book = Book(title = title, author = author, isbn = isbn, count = count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()

def add_member(name, email):
    print("Processing..")
    member = Member(name = name, email = email)
    session.add(member)
    session.commit()