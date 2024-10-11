# book_class.py

class Book:
    def __init__(self, title, author, year):
        # Initialize the book's title, author, and publication year
        self.title = title
        self.author = author
        self.year = year
        # You might want to print a friendly message when creating a book!
        # print(f"A new book '{self.title}' has been created!")

    def __del__(self):
        # When the book is deleted, let the user know
        print(f"Deleting {self.title}")

    def __str__(self):
        # This method returns a nice string representation for end users
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # This method returns a more technical string representation for developers
        return f"Book('{self.title}', '{self.author}', {self.year})"
