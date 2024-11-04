from crud import add_book, get_book
# ,add_member

def printBooks():
    books = get_book()
    for book in books:
        available = "Available" if book.count > 0 else "Not available"
        print(f"{book.id}: '{book.title}' by {book.author} (ISBN: f{book.isbn}) -  {available} ({book.count} copies)")


def addNewBook():
    title = input("Enter title of the book: ")
    author = input("Enter author name of the book: ")
    isbn = input("Enter ISBN number of the book: ")
    count = int(input("Enter total number of the books required: "))
    add_book(title, author, isbn, count)

def main():
    print("************************")
    print("1. Add a Book")
    print("2. View a book")
    print("************************")
    choice = input("Enter your choice: ")

    if choice == '1':
        addNewBook()
    
    # elif choice == '2':
    #     name = input("Enter title of the book: ")
    #     email = input("Enter author name of the book: ")
    #     add_member(name, email)
    
    elif choice == '2':
        printBooks()
    else:
        print("Wrong choice entered!!")


if __name__ == "__main__":
    main()






