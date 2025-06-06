class Publication:
    
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

    def get_publication_info(self):
        return f"Title: {self.title}, Year: {self.publication_year}"
        

class Book(Publication):
    material = "Paper"
    
    def __init__(self, title, author, publication_year):
        super().__init__(title, publication_year)
        self.author = author
        self.is_borrowed = False

    def display_book_info(self):
        publication_info = self.get_publication_info()
        print(f"{publication_info}, Author: {self.author}")
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

my_novel = Book("The Great Adventure", "Jane Doe", 2023)
my_novel.display_book_info()
my_novel.borrow_book()
my_novel.display_book_info()
print(isinstance(my_novel, (Book, Publication)))
print(issubclass(Book, Publication))