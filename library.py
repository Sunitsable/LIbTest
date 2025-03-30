class Library:
    def __init__(self):
        """Initialize a library with an empty book catalog."""
        self.books = {}
    
    def add_book(self, title, copies=1):
        """Add a book to the library with a specified number of copies."""
        if copies <= 0:
            raise ValueError("Number of copies must be positive.")
        self.books[title] = self.books.get(title, 0) + copies
    
    def borrow_book(self, title):
        """Borrow a book if available."""
        if title not in self.books or self.books[title] == 0:
            raise ValueError("Book not available.")
        self.books[title] -= 1
    
    def return_book(self, title):
        """Return a borrowed book."""
        if title not in self.books:
            self.books[title] = 0
        self.books[title] += 1
    
    def is_book_available(self, title):
        """Check if a book is available."""
        return self.books.get(title, 0) > 0
