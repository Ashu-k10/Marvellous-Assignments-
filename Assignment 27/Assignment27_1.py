class Bookstore:

    # Class variable
    Books = 0

    def __init__(self, name, Author):
        self.name = name
        self.Author = Author

        # Increment book count
        Bookstore.Books += 1

    def display(self):
        print(f"{self.name} by {self.Author}. No of books: {Bookstore.Books}")


# Create first object
obj1 = Bookstore("Linux System Programming", "Robert Love")
obj1.display()

# Create second object
obj2 = Bookstore("Python Programming", "Guido van Rossum")
obj2.display()