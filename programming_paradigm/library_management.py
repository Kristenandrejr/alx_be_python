class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        """Initialize a book with a title and an author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
            return False
        self._is_checked_out = True
        print(f"You have checked out '{self.title}'.")
        return True

    def return_book(self):
        """Mark the book as returned."""
        if not self._is_checked_out:
            print(f"'{self.title}' was not checked out.")
            return False
        self._is_checked_out = False
        print(f"You have returned '{self.title}'.")
        return True

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Represents a library that contains a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        print(f"Book titled '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """Return a checked-out book by its title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        print(f"Book titled '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books in the library.")


# Example of how the classes interact with each other
if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Listing available books
    print("\nAvailable books after setup:")
    library.list_available_books()

    # Checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
