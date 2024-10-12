# library_system.py

# Define the base class for books
class Book:
    def __init__(self, title, author):
        # Initialize the book's title and author
        self.title = title
        self.author = author

    def __str__(self):
        # Return a friendly string representation of the book
        return f"Book: {self.title} by {self.author}"


# Define an EBook class that inherits from Book
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the parent class's initializer
        super().__init__(title, author)
        # Add a specific attribute for EBooks
        self.file_size = file_size

    def __str__(self):
        # Return a string representation for the EBook
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Define a PrintBook class that also inherits from Book
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the parent class's initializer
        super().__init__(title, author)
        # Add a specific attribute for PrintBooks
        self.page_count = page_count

    def __str__(self):
        # Return a string representation for the PrintBook
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Define the Library class to manage the books
class Library:
    def __init__(self):
        # Initialize an empty list to hold our books
        self.books = []

    def add_book(self, book):
        # Add a book (or EBook or PrintBook) to the library
        self.books.append(book)

    def list_books(self):
        # Print details of each book in the library
        for book in self.books:
            print(book)
