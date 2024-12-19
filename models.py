class Author:
    authors = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, id, name):
        if name == "":
            print("Error: Author name cannot be empty.")
            return None
        for author in cls.authors:
            if author.name == name:
                print(f"Error: Author with the name {name} already exists.")
                return None
        author = Author(id, name)
        cls.authors.append(author)
        print(f"Author '{name}' created successfully.")
        return author

    @classmethod
    def delete(cls, id):
        for author in cls.authors:
            if author.id == id:
                cls.authors.remove(author)
                print(f"Author with ID {id} deleted successfully.")
                return
        print("Error: Author not found.")

    @classmethod
    def get_all(cls):
        return cls.authors

    @classmethod
    def find_by_id(cls, id):
        for author in cls.authors:
            if author.id == id:
                return author
        print("Error: Author not found.")
        return None


class Book:
    books = []

    def __init__(self, id, title, author, publisher, year_of_publication):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year_of_publication = year_of_publication

    @classmethod
    def create(cls, id, title, author, publisher, year_of_publication):
        if title == "":
            print("Error: Book title cannot be empty.")
            return None
        for book in cls.books:
            if book.title == title:
                print(f"Error: Book with title '{title}' already exists.")
                return None
        book = Book(id, title, author, publisher, year_of_publication)
        cls.books.append(book)
        print(f"Book '{title}' created successfully.")
        return book

    @classmethod
    def delete(cls, id):
        for book in cls.books:
            if book.id == id:
                cls.books.remove(book)
                print(f"Book with ID {id} deleted successfully.")
                return
        print("Error: Book not found.")

    @classmethod
    def get_all(cls):
        return cls.books

    @classmethod
    def find_by_id(cls, id):
        for book in cls.books:
            if book.id == id:
                return book
        print("Error: Book not found.")
        return None

    @classmethod
    def get_books_by_author(cls, author):
        books_by_author = [book for book in cls.books if book.author == author]
        return books_by_author