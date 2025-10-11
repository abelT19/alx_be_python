class Book:
    # Class variable to count total books
    total_books = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __del__(self):
        print(f"Book '{self.title}' has been deleted.")
        Book.total_books -= 1
