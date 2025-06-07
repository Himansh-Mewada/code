class Publication:
    
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

    def get_publication_info(self):
        return f"Title: {self.title}, Year: {self.publication_year}"
    
    def display_item(self):
        print(f"Item type: Generic Publication, {self.get_publication_info()}")
        

class Book(Publication):
    material = "Paper"
    
    def __init__(self, title, author, publication_year):
        super().__init__(title, publication_year)
        self.author = author
        self.is_borrowed = False

    def display_item(self):
        super().display_item()
        print(f"Author: {self.author}")
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

class Magazine(Publication):
    def __init__(self, title, publication_year, issue_number):
        super().__init__(title, publication_year)
        self.issue_number = issue_number

    def display_item(self):
        super().display_item()
        print(f"Issue Number: {self.issue_number}")


library_items = [
    Book("The Python Journey", "A. Programmer", 2023),
    Magazine("Tech Weekly", 2024, 45),
    Book("OOP Made Easy", "B. Coder", 2022),
    Magazine("Science Today", 2025, 101)
]

for items in library_items:
    items.display_item()