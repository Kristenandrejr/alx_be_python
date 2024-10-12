# library_system.py

# Base class for books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"

# Subclass for eBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Subclass for printed books
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class to hold a collection of books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty!")
        else:
            for book in self.books:
                print(book.get_info())
