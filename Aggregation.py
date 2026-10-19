class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(f"- {book.title} by {book.author}")


book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")


my_library = Library("City Central Library")


my_library.add_book(book1)
my_library.add_book(book2)


my_library.show_books()


del my_library


print("\n--- Library deleted ---")
print(f"Independent book status: '{book1.title}' still exists in memory.")