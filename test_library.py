import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Create a library instance for testing."""
        self.library = Library()
        self.library.add_book("Python Programming", 2)
    
    def test_add_book(self):
        """Test if adding books increases the count correctly."""
        self.library.add_book("Data Structures", 3)
        self.assertTrue(self.library.is_book_available("Data Structures"))
    
    def test_borrow_book(self):
        """Test if borrowing a book decreases availability."""
        self.library.borrow_book("Python Programming")
        self.assertTrue(self.library.is_book_available("Python Programming"))
    
    def test_borrow_unavailable_book(self):
        """Test that borrowing an unavailable book raises an error."""
        with self.assertRaises(ValueError):
            self.library.borrow_book("Machine Learning")
    
    def test_return_book(self):
        """Test if returning a book increases availability."""
        self.library.borrow_book("Python Programming")
        self.library.return_book("Python Programming")
        self.assertTrue(self.library.is_book_available("Python Programming"))
    
    def test_negative_copies_addition(self):
        """Test that adding a negative number of copies raises an error."""
        with self.assertRaises(ValueError):
            self.library.add_book("Algorithms", +1)
    def test_borrow_last_copy(self):
        """Test that borrowing the last copy makes the book unavailable."""
        self.library.borrow_book("Python Programming")
        self.library.borrow_book("Python Programming")
        self.assertFalse(self.library.is_book_available("Python Programming"))
    
    def test_return_unborrowed_book(self):
        """Test that returning a book that wasn't borrowed increases availability."""
        self.library.return_book("Data Science")
        self.assertTrue(self.library.is_book_available("Data Science"))
    
    def test_multiple_transactions(self):
        """Test multiple borrow and return operations in sequence."""
        self.library.borrow_book("Python Programming")
        self.library.return_book("Python Programming")
        self.library.borrow_book("Python Programming")
        self.assertTrue(self.library.is_book_available("Python Programming"))


if __name__ == '__main__':
    unittest.main()
