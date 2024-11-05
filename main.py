from crud import add_book, get_book, add_member, get_member, issue_book, return_book, get_transactions_by_member


def addNewBook():
    title = input("Enter title of the book: ")
    author = input("Enter author name of the book: ")
    isbn = input("Enter ISBN number of the book: ")
    count = int(input("Enter total number of the books required: "))
    add_book(title, author, isbn, count)
    print("> New book has been added <")


def viewBook():
    books = get_book()
    for book in books:
        available = "Available" if book.count > 0 else "Not available"
        print(f"{book.id}: '{book.title}' by {book.author} (ISBN: f{book.isbn}) -  {available} ({book.count} copies)")


def addNewMember():
    name = input("Enter name of the member: ")
    email = input("Enter email id of the member: ")
    add_member(name, email)
    print("> New member has been added <")


def viewMember():
    member = get_member()
    for member in member:
        print(f"{member.id} {member.name} (Email id: {member.email})")


def issueABook():
    book_id = int(input("Enter book id of required book: "))
    member_id = int(input("Enter required member id: "))
    issue_book(book_id, member_id)

def returnABook():
    transaction_id = int(input("Enter transaction id: "))
    return_book(transaction_id)

def getTransactionForMember():
    member_id = int(input("Enter member ID: "))
    transactions = get_transactions_by_member(member_id)
    for transactions in transactions:
        return_status = "Returned" if transactions.return_date else "Not returned"
        print(f"Transaction id: {transactions.id}, Book id: {transactions.book_id}, Issue date: f{transactions.issue_date}, Return date: f{transactions.return_date}, Status: f{return_status}")

def main():
    while True:
        print("************************")
        print("1. Add a Book")
        print("2. View a book")
        print("3. Add a member")
        print("4. View member")
        print("5. Issue book")
        print("6. Return book")
        print("7. View transactions made by member")
        print("8. Exit program")
        print("************************")
        choice = input("Enter your choice: ")

        if choice == '1':
            addNewBook()    
        elif choice == '2':
            viewBook()
        elif choice == '3':
            addNewMember()
        elif choice == '4':
            viewMember()
        elif choice == '5':
            issueABook()
        elif choice == '6':
            returnABook()
        elif choice == '7':
            getTransactionForMember()
        elif choice == '8':
            break
        else:
            print("Wrong choice entered!!")


if __name__ == "__main__":
    main()






