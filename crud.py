from models import Book, Member, Transactions
from database import session
from datetime import date

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

def get_member():
    return session.query(Member).all()

def issue_book(book_id, member_id):
    book = session.query(Book).filter_by(id = book_id).first()
    if book and book.count > 0:
        transaction = Transactions(book_id = book_id, member_id = member_id, issue_date = date.today())
        book.count -= 1
        session.add(transaction)
        session.commit()
        print("> Book issued <")
    else:
        print("> Book not available for issue <")

def return_book(transaction_id):
    transaction = session.query(Transactions).filter_by(id = transaction_id).first()
    if transaction and not transaction.return_date:
        transaction.return_date = date.today()
        book = session.query(Book).filter_by(id = transaction.book_id).first()
        book.count += 1
        session.commit()
        print("> Book returned to library <")
    else:
        print("> Book already returned <")

def get_transactions_by_member(member_id):
    return session.query(Transactions).filter_by(member_id = member_id).all()
    