# File: book_class.py

class Book:
    """
    A class to represent a book with a title, author, and publication year.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """

    def __init__(self, title, author, year):
        """
        Initializes a Book instance with the provided title, author, and year.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor that is called when an instance is deleted.
        Prints a message indicating the deletion of the book.
        """
        print(f"Deleting '{self.title}'")

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        
        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the book that could be used to recreate it.
        
        Returns:
            str: A string in the format "Book('title', 'author', year)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
