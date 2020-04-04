=> Python is an object oriented programming language.

=> almost everything in Python is an object, with its properties and methods.

class MyClass:
  x = 5

 p1 = MyClass()
print(p1.x) 


# __init__() Function
 => Use the __init__() function to assign values to object properties, 
 or other operations that are necessary to do when the object is being created:

 class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person('Manish',38)
p1.age


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print(f"My name is {self.name} and I am {self.age} aged")
p = person('Singh',38)
p.myfunc()

=> The __init__() function is called automatically every time the class is being used to create a new object.

# pass => Helps excape giving definations
class Person:
  pass 

 ## Inheritance allows us to define a class that inherits all the methods and properties from another class.

 class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(f"Full name = {self.firstname} {self.lastname}")

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname) => spuer() will initiate parent class __init__ method.
        self.year = year
        
    def printall(self):
        print(f"{self.firstname} {self.lastname} graduation Year is {self.year}")

p = student('Manish','Singh',2005)
p.printname()
p.printall()

Full name = Manish Singh
Manish Singh graduation Year is 2005

## Polymorphism / Inheritence

class Animal:
    def __init__(self,name):
        self.name = name 
    def bark(self):
        raise NotImplementedError("Please implement this method")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says WHOOF !!")

mydog = Dog("Frankie")
mydog.bark() => Frankie says WHOOF !!



class Book:
    def __init__(self,title,author,page):
        self.title = title
        self.author = author
        self.page = page
    
    def __str__(self): => Special function  for representing object into string formatt
        return f"{self.title} is written by {self.author}"

    def __len__(self): => special function for inbuild len represetation for user defined class.
        return self.page

mybook = Book('Python','Jose',78)
print(mybook) => Python is written by Jose
len(mybook) => 78 

=====================================================
## Simple Programm 
class Account:
    
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Total balance : {self.balance}")
    def withdraw(self,amount):
        if (self.balance >=  amount):
            self.balance = self.balance - amount
            print(f"Total balance : {self.balance}")
        else:
            print("Not sufficient balance")
    def check_balance(self):
        return self.balance
    
        
    def __str__(self):
        return f"""Account owner : {self.name}
Account balance : ${self.balance}
        """

myaccount = Account('Manish',100)
myaccount.check_balance()
myaccount.deposit(200)
myaccount.withdraw(300)
print(myaccount)