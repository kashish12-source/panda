'''here we are buliding a library management system using python'''
'''which contain the following features:
1] add book
2] delete book
3] view all books
4] search for a book        
'''
import pandas as pd

class Library:
   
    def add(self,bookname):
        self.bookname=bookname
        with open('students.csv','a')as f:
            f.write(bookname)
        print('book has been added successfully')
    def view(self):
        with open('students.csv')as f:
            print(f.read())

            
    def delete(self,booknumber):
        self.booknumber=booknumber
        with open('students.csv','w')as f:
            
            if self.booknumber in f:
                f.write("return")
    def search_book(self, bookname):
        with open("students.csv", "r") as f:
            books = f.read()

        if bookname in books:
            print("Book is available")
        else:
            print("Book not found")
book=Library()
choice=int(input('select what you want to do \n1] add book (1)\n2] delete book (2)\n3] search book (3)\n4] view'))

if choice==1:
   
    bookName=input('enter the name of the book here:')
    book.add(bookName)
elif choice==2:
    booknumber=int(input('enter the number of book here :'))
    book.delete(booknumber)
elif choice==3:
    bookname=input('enter the book name :')
    book.search_book(bookname)
elif choice==4:
    book.view()
else:
    print('Please choose the option')




