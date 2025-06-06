class Book:
    material = "Paper"

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_book_info(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        if self.is_borrowed == True:
            print("Availability: Not Available")
        else:
            print("Availability: Available")

    def borrow_book(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} could not be borrowed.")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is currently already in the library.")


book1 = Book("The Python Journey",  "A. Programmer")
book2 = Book("OOP Made Easy", "B. Coder")
book1.display_book_info()
book2.display_book_info()
book1.borrow_book()
book1.display_book_info()
book1.borrow_book()
book1.return_book()
book1.display_book_info()
book2.return_book()