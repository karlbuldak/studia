# Write a program in which define a class that describes states and behaviors of an  e-book.
# Each book has a title, author, number of pages and the current page number that is
# currently being read.
# It is possible to open a book - then we can read it.
# If a book is open, it is possible to go to the next or previous page.

class Ebook():
    
    def __init__(self, title, author, num_of_pages):
        
        self.title=title
        self.author=author
        self.num_of_pages=num_of_pages
        self.curr_page_num=0
        self.open=False
        
    def open_ebook(self):
        if self.open==False:
            self.open=True
        else:
            print('Book already opened')
            
    def close_ebook(self):
        if self.open==False:
            print('Book already closed')
        else:
            self.open=False
            
    def status(self):
        if self.open==True:
            print(f"The book is opened, it's title is {self.title}, it's author is {self.author}, it's {self.num_of_pages} pages long, you're on page number {self.curr_page_num}")
        if self.open==False:
            print(f"The book is closed, it's title is {self.title}, it's author is {self.author}, it's {self.num_of_pages} pages long, you're on page number {self.curr_page_num}")
            
    def read_ebook(self):
        if self.curr_page_num!=self.num_of_pages:
            if self.open==True:
                self.curr_page_num+=1
            if self.open==False:
                print("You can't read from a closed book!")
        else:
            print('You finished the whole book!')
