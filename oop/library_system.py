# library_system.py

# Let's start with a base class that represents a general book.
class Book:
    def __init__(self, title, author):
        # Initialize the book with a title and an author
        self.title = title
        self.author = author

    def get_info(self):
        # Return a formatted string with book details
        return f"Book: {self.title} by {self.author}"

# Now, let's create a subclass specifically for eBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the parent class's initializer for title and author
        super().__init__(title, author)
        # Additional attribute for file size in KB
        self.file_size = file_size

    def get_info(self):
        # Override to include file size in the details
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Another subclass for print books, which have pages instead of file size
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the parent class's initializer
        super().__init__(title, author)
        # Additional attribute for page count
        self.page_count = page_count

    def get_info(self):
        # Override to include page count in the details
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Finally, our Library class uses composition to manage a collection of books
class Library:
    def __init__(self):
        # Initialize an empty list to store book instances
        self.books = []

    def add_book(self, book):
        # Add a book to the library's collection
        self.books.append(book)

    def list_books(self):
        # Print details of each book in the library
        if not self.books:
            print("The library is empty!")
        else:
            for book in self.books:
                print(book.get_info())
