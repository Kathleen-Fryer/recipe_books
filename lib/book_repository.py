from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            book = Book(row["id"], row["title"], row["author"], row["release_year"])
            books.append(book)
        return books
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM books WHERE id = %s',
            [id]
        )
        row = rows[0]
        return Book(
            row["id"],
            row["title"],
            row["author"],
            row["release_year"]
        )
    
    def create(self, space):
        print("in create function")
        self._connection.execute('INSERT INTO spaces (name, price, details, img_link, user_id) VALUES (%s, %s, %s, %s, %s)', [space.name, space.price, space.details, space.img_link, space.user_id])
        return None    
    
