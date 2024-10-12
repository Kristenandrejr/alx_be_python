# library_system.py

# Let's start by defining our base class for books!
class Book:
    def __init__(self, title, author):
        # Initialize the book's title and author
        self.title = title
        self.author = author
        print(f"Creating a new book: '{self.title}' by {self.author}.")

    def __str__(self):
        # This method returns a friendly string representation of the book
        return f"Book: {self.title} by {self.author}"


# Now, let's create an EBook class that inherits from Book!
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the parent class's initializer
        super().__init__(title, author)
        # Add a specific attribute for EBooks
        self.file_size = file_size
        print(f"Creating an EBook: '{self.title}', Size: {self.file_size}KB.")

    def __str__(self):
        # Return a string representation for the EBook
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Next, we'll create a PrintBook class, also inheriting from Book.
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the parent class's initializer
        super().__init__(title, author)
        # Add a specific attribute for PrintBooks
        self.page_count = page_count
        print(f"Creating a PrintBook: '{self.title}', Pages: {self.page_count}.")

    def __str__(self):
        # Return a string representation for the PrintBook
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Now, let’s create our Library class to manage these books!
class Library:
    def __init__(self):
        # Initialize an empty list to hold our books
        self.books = []
        print("A new library has been created!")

    def add_book(self, book):
        # Add a book (or EBook or PrintBook) to our library
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        # Print details of each book in the library
        print("\nListing all books in the library:")
        for book in self.books:
            print(book)
