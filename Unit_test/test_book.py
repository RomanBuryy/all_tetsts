import unittest
from book import Book, Bookshelf



class TestBook(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book("Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future", "Ashlee Vance")
        self.book_2 = Book("The Alchemist", "Paulo Coelho")
        self.bookshelf = Bookshelf("Test bookshelf")

    def test_book(self):
        self.assertEqual(self.book_1.__str__(),
                         "Book: Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future, Author: Ashlee Vance")
        self.assertEqual(self.book_2.__str__(),
                         "Book: The Alchemist, Author: Paulo Coelho")
        self.assertEqual(self.book_1.book_name, "Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future")
        self.assertEqual(self.book_1.book_author, "Ashlee Vance")
        self.assertEqual(self.book_2.book_author, "Paulo Coelho")
        self.assertEqual(self.book_2.book_name, "The Alchemist")

    def test_bookshelf(self):
        self.assertEqual(self.bookshelf.__str__(), "Test bookshelf")

    def test_bookshelf_add(self):
        self.bookshelf += self.book_1
        self.bookshelf += self.book_2


