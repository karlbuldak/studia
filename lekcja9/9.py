class book():
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year

class ebook(book):
    def __init__(self, title, author, year, filename):
        self.filename=filename
        super().__init__(title)
        super().__init__(author)
        super().__init__(year)
    def __str__(self):
        return("It's an e-book, it's details: " + "title: " + self.title+"author: " + self.author + "year: " + self.year+"filename: " + self.filename)
    
test=ebook('a','b','c','d')
print(ebook)