from tkinter import*
root=Tk()
root.geometry("400x400")
root.title("class")
class Bookshelf:
    def __init__(self,author,name,price,publishyear):
        self.book_name=name
        self.book_author=author
        self.book_price=price
        self.book_publish=publishyear
    def add_book(self):
        print("Name:"+self.book_name)
        print("Author:"+self.book_author)
        print("Price:"+str(self.book_price))
        print("Publish Year: "+str(self.book_publish))
        print("\n")
b1=Bookshelf("Harry Potter and the Philsopher's stone","J.K.Rowling","$19.28","1997")
b1.add_book()
b2=Bookshelf("Percy Jackson and the Lightning Theif","Rick Riodan","$16.99","2005")
b2.add_book()