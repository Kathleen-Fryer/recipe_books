class Book:
    def __init__(self,id, title, author, release_year):
        self.id = id
        self.title = title
        self.author = author
        self.release_year = release_year

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author}, {self.release_year})"


