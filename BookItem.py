# -*- coding: utf-8 -*-
class BookItem:
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack

    def RequestBook(self,name):
        self.issueBook = name
        
    def returnBook(self,name):
        self.returnBook = name