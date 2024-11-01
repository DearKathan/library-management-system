from crud import add_book

def main():
    print("************************")
    print("1. Add a Book")
    print("2. View a book")
    print("************************")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter title of the book: ")
        author = input("Enter author name of the book: ")
        isbn = input("Enter ISBN number of the book: ")
        count = int(input("Enter total number of the books required: "))
        add_book(title, author, isbn, count)
    
    elif choice == '2':
        print("Code to view book")
    else:
        print("WRONG CHOICE ENTERED!!")


if __name__ == "__main__":
    main()






