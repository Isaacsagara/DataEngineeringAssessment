"""
This module contains classes for library management system.

@author: Isaac Sagara
"""

# Class represents a single book in the library
class LibraryBook:
    def __init__(self, title, author, pub_year, isbn):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.isbn = isbn
        self.available = True
        
# Class represents a library
class Library:
    def __init__(self):
        self.books = []
        self.total_books = 0
        self.available_books = 0

# Method to add a book in library
    def add_book(self, title, author, pub_year, isbn):
        book = LibraryBook(title, author, pub_year, isbn)
        self.books.append(book)
        self.total_books += 1
        print("Book added successfully")
        
# Method to remove a book in library
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.total_books -= 1
                print("Book removed successfully")
                return
        print("Book not found")

# Method to search a book in library
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Title:", book.title)
                print("Author:", book.author)
                print("Publication Year:", book.pub_year)
                print("ISBN:", book.isbn)
                  
                if book.available:
                    print("Availability: Available")
                else:
                    print("Availability: Not Available")
                return
        print("Book not found")
        
# Method to display all books in library
    def display_all_books(self):
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("Publication Year:", book.pub_year)
            print("ISBN:", book.isbn)
            if book.available:
                print("Availability: Available")
                print('-'*35)  

            else:
                print("Availability: Not Available")

# Method to check out the book
    def checkout_book(self, title):
            for book in self.books:
                if book.title == title:
                    if book.available:
                        book.available = False
                        self.available_books -= 1
                        print("Book checked out successfully")
                    else:
                        print("Book not available")
                    return
            print("Book not found")

# Method to check in the book    
    def checkin_book(self, title):
            for book in self.books:
                if book.title == title:
                    if not book.available:
                        book.available = True
                        self.available_books += 1
                        print("Book checked in successfully")
                    else:
                        print("Book already available")
                    return
            print("Book not found")
        
# Method to update all books in library
    def update_availability(self, title, available):
        for book in self.books:
            if book.title == title:
                book.available = available
                if available:
                    print("Book is now available")
                else:
                    print("Book is now not available")
                return
        print("Book not found")
        

# Usage example:
library = Library()

# Add books
library.add_book("Python", "John Smith", 2021, "123456789")
library.add_book("Data Science", "Jane Doe", 2020, "987654321")
library.add_book("Python for Machine Learning", "Mark Brown", 2019, "543210987")
print('*'*30)

# Display all books
library.display_all_books()
print('*'*30)

# Search for a book
library.search_book("Python")
print('*'*30)

# Remove a book
library.remove_book("Data Science")
print('*'*30)

# Checkout a book
library.checkout_book("Python for Machine Learning")
print('*'*30)

# Checkin a book
library.checkin_book("Python for Machine Learning")
print('*'*30)

# Update book availability
library.update_availability("Python for Machine Learning", True)
print('*'*30)

# Display all books
library.display_all_books()
print('*'*30)
