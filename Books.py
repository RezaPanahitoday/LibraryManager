class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Authoer: {self.author}")
        print(f"Year: {self.year}")
        print(f"Copies: {self.copies}")


number_1 = Book("Programing", "Reza Panahi", 2020, 5)
number_1.display_info()
