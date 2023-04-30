#!/usr/bin/env python
# coding: utf-8

# #question 1

# #In object-oriented programming, a class is a blueprint or a template for creating objects that encapsulates data (attributes) and behavior (methods) that operate on that data. An object, on the other hand, is an instance of a class that contains its own unique set of data and can execute its own set of methods.

# In[ ]:


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def walk(self):
        print(self.name + " is walking.")
        
    def talk(self):
        print(self.name + " is talking.")
        
    def eat(self, food):
        print(self.name + " is eating " + food + ".")


# #question 2

# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

# #question 3

# In Python, the function is a special method that is automatically called when an object is created from a class. It is used to initialize the attributes of the object

# In[1]:


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def walk(self):
        print(self.name + " is walking.")
        
    def talk(self):
        print(self.name + " is talking.")
        
    def eat(self, food):
        print(self.name + " is eating " + food + ".")


# #question 4

# self is a reference to the current object. It is used to access the attributes and methods of the object within its own methods.

# n object-oriented programming (OOP), attributes and methods are the two primary components of a class, which is a blueprint for creating objects.
# 
# Attributes are the properties of an object that define its state. They are represented by variables inside a class and store the data associated with the object. For example, if we define a Car class, its attributes might include the make, model, year, color, and price of the car. We define attributes using the self keyword inside the class methods, and access them using the dot notation with the object name.
# 
# Methods, on the other hand, are functions that define the behavior of an object. They are also defined inside a class and operate on the attributes of the class. Methods can be used to modify the state of the object or perform some operation on it. For example, if we define a Car class, its methods might include start(), stop(), accelerate(), and brake(). We define methods using the def keyword inside the class, and access them using the dot notation with the object name.
# 
# Here is an example of a Car class with attributes and methods:

# In[2]:


class Car:
    def __init__(self, make, model, year, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        
    def start(self):
        print(f"The {self.color} {self.make} {self.model} is starting.")
        
    def stop(self):
        print(f"The {self.color} {self.make} {self.model} is stopping.")
        
    def accelerate(self, speed):
        print(f"The {self.color} {self.make} {self.model} is accelerating to {speed} mph.")
        
    def brake(self):
        print(f"The {self.color} {self.make} {self.model} is braking.")


# #question 5

# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class to inherit the properties (attributes and methods) of another class. 
# Single inheritance
# Multilevel inheritance
# Multiple inheritance
# Hierarchical inheritance
