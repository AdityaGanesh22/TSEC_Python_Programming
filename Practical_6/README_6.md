# Practical 6 – Object-Oriented Programming (OOP) Primer

## 4.1 Introduction to OOP

Object-Oriented Programming (OOP) is a paradigm that models real-world systems using classes and objects. It emphasizes modularity, reusability, and efficiency.

### Classes and Objects
- A `class` is a blueprint that defines attributes (data) and methods (behavior).
- An `object` is an instance of a class, representing a specific entity in the system.

Example:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
print(book1.title, "-", book1.author)
```

Here, `Book` is the class, and `book1` is an object.

---

### Encapsulation
Encapsulation means bundling data and methods together and restricting direct access to internal details. Private attributes are hidden from outside interference, accessed only through methods.

Example:
```python
class LibraryMember:
    def __init__(self, name):
        self.__name = name   # private attribute

    def get_name(self):
        return self.__name

member = LibraryMember("Alice")
print(member.get_name())
```

---

### Inheritance
Inheritance allows one class to derive properties and methods from another, promoting code reuse.

Example:
```python
class Person:
    def __init__(self, name):
        self.name = name

class Librarian(Person):
    def manage_books(self):
        print(f"{self.name} manages the library collection.")

lib = Librarian("Mr. Sharma")
lib.manage_books()
```

---

### Polymorphism
Polymorphism allows different classes to define methods with the same name but different behavior.

Example:
```python
class Member(Person):
    def role(self):
        return "Borrows books"

class Librarian(Person):
    def role(self):
        return "Manages library"

p1 = Member("Alice")
p2 = Librarian("Mr. Sharma")

print(p1.role())
print(p2.role())
```
---

## 4.2 Creating Classes and Objects

### Class Attributes and Methods
Attributes represent data stored in the class. Methods define behavior or operations performed on the data.

Example:
```python
class Book:
    library_name = "Central Library"   # class attribute

    def __init__(self, title, author):
        self.title = title             # instance attribute
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author}"

book = Book("The Alchemist", "Paulo Coelho")
print(Book.library_name)
print(book.get_info())
```
---

### Constructor
A constructor initializes an object when it is created.

Example:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Book object created!")

book = Book("Inferno", "Dan Brown")
```
---

### Destructor
A destructor is called when an object is deleted or goes out of scope. It is useful for cleanup tasks.

Example:
```python
class Book:
    def __init__(self, title):
        self.title = title

    def __del__(self):
        print(f"Book '{self.title}' removed from memory.")

b = Book("Invisible Man")
del b
```
---

## 4.3 Types of Inheritance

Python supports several types of inheritance:

### Single Inheritance
A subclass inherits from one base class.

Example:
```python
class Person:
    def __init__(self, name):
        self.name = name

class Member(Person):
    def borrow_book(self):
        print(f"{self.name} borrows a book.")

m = Member("Alice")
m.borrow_book()
```
---

### Multiple Inheritance
A subclass inherits from more than one base class.

Example:
```python
class DigitalAccess:
    def access_online(self):
        print("Accessing online resources.")

class PhysicalAccess:
    def access_library(self):
        print("Accessing physical library.")

class HybridMember(DigitalAccess, PhysicalAccess):
    pass

h = HybridMember()
h.access_online()
h.access_library()
```
---

### Multilevel Inheritance
A subclass inherits from another subclass, forming a chain.

Example:
```python
class Person:
    def __init__(self, name):
        self.name = name

class Member(Person):
    def borrow_book(self):
        print(f"{self.name} borrows a book.")

class PremiumMember(Member):
    def borrow_special_collection(self):
        print(f"{self.name} borrows from the special collection.")

pm = PremiumMember("Sneha")
pm.borrow_book()
pm.borrow_special_collection()
```
---

## Summary

In this practical, you will:
- Learn how to define classes and create objects.
- Apply encapsulation to protect data and expose only necessary methods.
- Use inheritance to extend functionality and reuse code.
- Demonstrate polymorphism by overriding methods in subclasses.
- Explore constructors and destructors for object lifecycle management.
- Understand single, multiple, and multilevel inheritance.

The examples here (Library System) are meant to help you understand the concepts before you attempt the practical tasks on your own. In your tasks, you will apply these principles to scenarios like Event Management, Online Shopping, and Vehicle Rental Systems (any one of these).