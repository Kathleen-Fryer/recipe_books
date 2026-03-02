from lib.book import Book

"""
Book constructs with an id, title, author and release year
"""
def test_book_constructs():
    book = Book(1, "Test Title", "Test Author", 1996)
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.release_year == 1996


"""
Books format to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test Title", "Test Author", 1996)
    assert str(book) == "Book(1, Test Title, Test Author, 1996)"


"""
When two identical books are compared, they are equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test Title", "Test Author", 1996)
    book2 = Book(1, "Test Title", "Test Author", 1996)
    assert book1 == book2
