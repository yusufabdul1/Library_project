import sys
from models import Author, Book

def print_main_menu():
    print("\nWelcome to the Library Management System")
    print("1. Manage Authors")
    print("2. Manage Books")
    print("3. Exit")

def print_author_menu():
    print("\nManage Authors")
    print("1. Create Author")
    print("2. Delete Author")
    print("3. View All Authors")
    print("4. Find Author by ID")
    print("5. Back")

def print_book_menu():
    print("\nManage Books")
    print("1. Create Book")
    print("2. Delete Book")
    print("3. View All Books")
    print("4. View Books by Author")
    print("5. Find Book by ID")
    print("6. Back")

def manage_authors():
    while True:
        print_author_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            id = input("Enter Author ID: ")
            name = input("Enter Author Name: ")
            Author.create(id, name)
        elif choice == "2":
            id = input("Enter Author ID to delete: ")
            Author.delete(id)
        elif choice == "3":
            authors = Author.get_all()
            for author in authors:
                print(f"ID: {author.id}, Name: {author.name}")
        elif choice == "4":
            id = input("Enter Author ID to search: ")
            author = Author.find_by_id(id)
            if author:
                print(f"Author ID: {author.id}, Name: {author.name}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_books():
    while True:
        print_book_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author_name = input("Enter Author Name: ")
            publisher = input("Enter Publisher: ")
            year_of_publication = input("Enter Year of Publication: ")
            author = next((author for author in Author.get_all() if author.name == author_name), None)
            if author:
                Book.create(id, title, author, publisher, year_of_publication)
            else:
                print("Author not found.")
        elif choice == "2":
            id = input("Enter Book ID to delete: ")
            Book.delete(id)
        elif choice == "3":
            books = Book.get_all()
            for book in books:
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author.name}, Publisher: {book.publisher}, Year: {book.year_of_publication}")
        elif choice == "4":
            author_name = input("Enter Author Name to view their books: ")
            author = next((author for author in Author.get_all() if author.name == author_name), None)
            if author:
                books_by_author = Book.get_books_by_author(author)
                for book in books_by_author:
                    print(f"ID: {book.id}, Title: {book.title}")
            else:
                print("Author not found.")
        elif choice == "5":
            id = input("Enter Book ID to search: ")
            book = Book.find_by_id(id)
            if book:
                print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author.name}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print_main_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            manage_authors()
        elif choice == "2":
            manage_books()
        elif choice == "3":
            sys.exit("Come Back Anytime!👋😊")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()