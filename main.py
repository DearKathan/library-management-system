from crud import add_book, get_book, add_member, get_member


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


def main():
    print("************************")
    print("1. Add a Book")
    print("2. View a book")
    print("3. Add a member")
    print("4. View member")
    print("5. Issue book")
    print("6. Return book")
    print("7. View transactions made by member")
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

    # elif choice == '5':

    # elif choice == '6':

    # elif choice == '7':

    else:
        print("Wrong choice entered!!")


if __name__ == "__main__":
    main()






