"""Ebookstore Database Initialization Script"""

import sqlite3


def initialize_db():
    """Initialize the database and table structure"""
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    # Create table with all required columns
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    ''')

    # Make sure the table was created successfully
    cursor.execute("PRAGMA table_info(books)")
    columns = cursor.fetchall()
    print("\nTable structure verified:")
    for col in columns:
        print(f"{col[1]} ({col[2]})")

    # Insert sample data
    initial_books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and '
               'the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]

    try:
        cursor.executemany('INSERT INTO books VALUES (?,?,?,?)', initial_books)
        db.commit()
        print(f"\nSuccessfully inserted {len(initial_books)} sample books")
    except sqlite3.Error as e:
        print(f"\nError inserting books: {e}")

    return db


def get_valid_input(prompt, input_type=str):
    """Get and validate user input"""
    while True:
        try:
            value = input(prompt)
            if input_type == int:
                return int(value)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a {'number' if input_type == int else 'value'}.")


def add_book(db):
    """Add a new book to the database"""
    print("\n--- ADD NEW BOOK ---")
    try:
        book_id = get_valid_input("Enter book ID (number): ", int)
        title = get_valid_input("Enter book title: ")
        author = get_valid_input("Enter author name: ")
        qty = get_valid_input("Enter quantity (number): ", int)

        cursor = db.cursor()
        cursor.execute('INSERT INTO books VALUES (?,?,?,?)', (book_id, title, author, qty))
        db.commit()
        print(f"Successfully added '{title}' to the database!")
    except sqlite3.IntegrityError:
        print("Error: A book with this ID already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_book(db):
    """Update existing book information"""
    print("\n--- UPDATE BOOK ---")
    book_id = get_valid_input("Enter book ID to update: ", int)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
    book = cursor.fetchone()

    if book:
        print("\nCurrent details:")
        print(f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQty: {book[3]}")

        new_title = input("Enter new title (leave blank to keep current): ") or book[1]
        new_author = input("Enter new author (leave blank to keep current): ") or book[2]
        new_qty = input("Enter new quantity (leave blank to keep current): ")
        new_qty = int(new_qty) if new_qty else book[3]

        cursor.execute('''
            UPDATE books
            SET title=?, author=?, qty=?
            WHERE id=?
        ''', (new_title, new_author, new_qty, book_id))
        db.commit()
        print("Book updated successfully!")
    else:
        print("Book not found.")


def delete_book(db):
    """Delete a book from the database"""
    print("\n--- DELETE BOOK ---")
    book_id = get_valid_input("Enter book ID to delete: ", int)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
    book = cursor.fetchone()

    if book:
        print(f"\nFound book: {book[1]} by {book[2]}")
        confirm = input("Are you sure you want to delete this book? (y/n): ").lower()
        if confirm == 'y':
            cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
            db.commit()
            print("Book deleted successfully!")
    else:
        print("Book not found.")


def search_books(db):
    """Search for books in the database"""
    print("\n--- SEARCH BOOKS ---")
    print("1. Search by ID")
    print("2. Search by Title")
    print("3. Search by Author")
    choice = get_valid_input("Choose search method (1-3): ", int)

    cursor = db.cursor()
    if choice == 1:
        book_id = get_valid_input("Enter book ID: ", int)
        cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
    elif choice == 2:
        title = input("Enter title or part of title: ")
        cursor.execute('SELECT * FROM books WHERE title LIKE ?', (f'%{title}%',))
    elif choice == 3:
        author = input("Enter author or part of author name: ")
        cursor.execute('SELECT * FROM books WHERE author LIKE ?', (f'%{author}%',))
    else:
        print("Invalid choice")
        return

    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"ID: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nQty: {book[3]}\n")
    else:
        print("No books found.")


def main():
    """Main program loop"""
    db = initialize_db()

    while True:
        print("\n==== BOOKSTORE MANAGEMENT SYSTEM ====")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Books")
        print("0. Exit")

        choice = get_valid_input("Enter your choice (0-4): ", int)

        if choice == 1:
            add_book(db)
        elif choice == 2:
            update_book(db)
        elif choice == 3:
            delete_book(db)
        elif choice == 4:
            search_books(db)
        elif choice == 0:
            print("Closing database connection...")
            db.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
