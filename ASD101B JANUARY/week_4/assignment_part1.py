# Write a class definition named . The  class should have data attributes for a book’s title, the author’s name, and the publisher’s name. The class should also have the following: 
#   An  method for the class. The method should accept an argument for
# each of the data attributes.
#   Accessor and mutator methods for each data attribute.     
#   An  method that returns a string indicating the state of the object.

class Book:

 def __init__(self,title: str,author: str,publisher: str):
        self.title = title
        self.author = author
        self.publisher = publisher

 @property
 def title(self) -> str:
       return self.__title
 @title.setter
 def title(self,value: str):
        self.__title = value

 @property
 def author(self) -> str:
        return self.__author
 @author.setter
 def author(self,value: str):
        self.__author = value
        
 @property
 def publisher(self) -> str:
        return self.__publisher
 @publisher.setter
 def publisher(self, value: str):
        self.__publisher = value

 def __str__(self):
        return f"{{title: {self.title}, author: {self.author}, publisher:{self.publisher}}}"
my_book = Book("Infinite Jest", "David Foster Wallace", "Little,Brown, and Company")
print(my_book)
