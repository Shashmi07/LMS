import json

# Load saved books
def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist

# Save books to file
def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file)

# Add a book
def add_book(library_books, title, author, isbn):
    for book in library_books:
        if book['isbn'] == isbn:
            print(f"The book with ISBN {isbn} already exists.")
            return
    library_books.append({"title": title, "author": author, "isbn": isbn, "status": "available"})
    save_books(library_books)  # Save after adding a book
    print(f"The book '{title}' has been added to the library.")

# Borrow a book
def borrow_book(library_books, isbn, borrower_name):
    for book in library_books:
        if book['isbn'] == isbn:
            if book['status'] == 'available':
                book['status'] = 'borrowed'
                book['borrower_name'] = borrower_name
                save_books(library_books)  # Save after borrowing
                print(f"Book borrowed successfully by {borrower_name}")
                return
            else:
                print(f"Book with ISBN {isbn} is already borrowed.")
                return
    print(f"Book with ISBN {isbn} not found.")

# Display borrowed books
def view_borrowed_books(library_books):
    borrowed_books = [book for book in library_books if book['status'] == 'borrowed']
    if not borrowed_books:
        print("No books borrowed.")
    else:
        print("Borrowed Books:")
        for book in borrowed_books:
            print(f"Title: {book['title']}, Borrowed by: {book['borrower_name']}")

# Main function to interact with the system
def main():
    library_books = load_books()

    while True:
        print("-------Welcome to Library Management System-----------!")
        print("1. View all books")
        print("2. Available books")
        print("3. Borrow a book")
        print("4. Add a book")
        print("5. Return a book")
        print("6. View borrowed books")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if user_choice == 1:
            # View all books
            for book in library_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {book['status']}")
        elif user_choice == 2:
            # View available books
            available_books = [book for book in library_books if book['status'] == 'available']
            for book in available_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        elif user_choice == 3:
            isbn = input("Enter the book ISBN to borrow: ")
            borrower_name = input("Enter your name: ")
            borrow_book(library_books, isbn, borrower_name)
        elif user_choice == 4:
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN: ")
            add_book(library_books, title, author, isbn)
        elif user_choice == 6:
            # View borrowed books
            view_borrowed_books(library_books)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
