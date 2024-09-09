import datetime

# Display the current date and time when the program starts
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

print('Hello')
print('Welcome to Library Management System')

# Adding new books
book_list = [
    
    {'title': "The Hobbit", 'author': "J.R.R. Tolkien", 'isbn': "001", 'status': 'available', 'borrowed_time': None},
    {'title': "Treasure Island", 'author': "Robert Louis Stevenson", 'isbn': "002", 'status': 'available', 'borrowed_time': None},
    {'title': "The Call of the Wild", 'author': "Jack London", 'isbn': "003", 'status': 'available', 'borrowed_time': None},
    {'title': "Into the Wild", 'author': "Jon Krakauer", 'isbn': "004", 'status': 'available', 'borrowed_time': None},
    {'title': "Jurassic Park", 'author': "Michael Crichton", 'isbn': "005", 'status': 'available', 'borrowed_time': None}
]


def add_a_book():
    title = input("Enter book name: ")
    author = input("Enter author name: ")
    isbn = input("Enter book ISBN: ")
    books = {'title': title, 'author': author, 'isbn': isbn, 'status': 'available', 'borrowed_time': None}
    book_list.append(books)
    print(f'"{title}" book has been added to the library')

# Borrow books
def borrow():
    isbn = input("Enter book ISBN No: ")
    for book in book_list:
        if book['isbn'] == isbn:
            if book['status'] == 'available':
                book['status'] = 'borrowed'
                book['borrowed_time'] = datetime.datetime.now()
                print(f"This '{book['title']}' has been successfully borrowed at {book['borrowed_time'].strftime('%Y-%m-%d %H:%M:%S')}")
                return
            else:
                print(f"The book '{book['title']}' is currently unavailable")
                return
    print("Book not found")

# View available books
def available_books():
    print("\nAvailable books:")
    available_list = [book for book in book_list if book['status'] == 'available']
    if available_list:
        print("{:<30} {:<30} {:<15}".format('Title', 'Author', 'ISBN'))
        for book in available_list:
            print("{:<30} {:<30} {:<15}".format(book['title'], book['author'], book['isbn']))
    else:
        print("No available books")

# View borrowed books
def borrowed_books():
    print("\nBorrowed books:")
    borrowed_list = [book for book in book_list if book['status'] == 'borrowed']
    if borrowed_list:
        print("{:<30} {:<30} {:<15} {:<20}".format('Title', 'Author', 'ISBN', 'Borrowed Time'))
        for book in borrowed_list:
            print("{:<30} {:<30} {:<15} {:<20}".format(book['title'], book['author'], book['isbn'], book['borrowed_time'].strftime('%Y-%m-%d %H:%M:%S')))
    else:
        print("No borrowed books")

# Return book
def return_book():
    isbn = input("Enter book ISBN No: ")
    for book in book_list:
        if book['isbn'] == isbn:
            if book['status'] == 'borrowed':
                book['status'] = 'available'
                returned_time = datetime.datetime.now()
                print(f"This '{book['title']}' has been successfully returned at {returned_time.strftime('%Y-%m-%d %H:%M:%S')}")
                return
            else:
                print(f"The book '{book['title']}' is not borrowed")
                return
    print("Book not found")

# Main function
def main():
    while True:
        print("\n1. Add new book")
        print("2. Borrow a book")
        print("3. View available books")
        print("4. View borrowed books")
        print("5. Return book")
        print("6. Quit")
        
        select = input("Enter your choice: ")
        if select == "1":
            add_a_book()
        elif select == "2":
            borrow()
        elif select == "3":
            available_books()
        elif select == "4":
            borrowed_books()
        elif select == "5":
            return_book()
        elif select == "6":
            print('Thank you for using LMS. Have a great day!')
            break

main()
