class Book():
    def __init__(self, book_name: str, book_author: str):
        self.book_name = book_name
        self.book_author = book_author

    def __str__(self):
        return f"Book: {self.book_name}, Author: {self.book_author}"


class Bookshelf():
    book_shelf = []

    def __init__(self, description):
        self.description = description

    def __add__(self, book):
        self.book_shelf.append(book)
        return self

    def __str__(self):
        return f"{self.description}"

#
# a = Book("wwer", "eryrty")
# b = Book("werery", "ertert")
# c = Book("wetfgbhf", "ertewrt")
# d = Book("werwer", "ertyrtyu")
#
# some_shelf = Bookshelf("Test bookShelf")
# some_shelf += a
# some_shelf += b
# some_shelf += c
# print(some_shelf)
