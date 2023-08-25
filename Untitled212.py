#!/usr/bin/env python
# coding: utf-8

# #Question 1

# In[1]:


class vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle


# In[3]:


obj1=vehicle("TATA NANO", 40,20)


# In[4]:


obj1.average_of_vehicle


# In[5]:


obj1.max_speed


# In[6]:


obj1.name_of_vehicle


# #Question 2

# In[7]:


class Vehicle:
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Fuel Type: {self.fuel_type}")


# In[8]:


class Car(Vehicle):
    def __init__(self, name, fuel_type, brand):
        super().__init__(name, fuel_type)
        self.brand = brand

    def display_info(self): 
        super().display_info()
        print(f"Brand: {self.brand}")

    def seating_capacity(self, capacity):
        return f"{self.name} has a seating capacity of {capacity} people."


# In[9]:


my_car = Car(name="Sedan", fuel_type="Gasoline", brand="Toyota")
my_car.display_info()
print(my_car.seating_capacity(5))


# #Question 3

# #Multiple inheritance is a feature in object-oriented programming languages where a class can inherit attributes and methods from more than one parent class. In other words, a class can have multiple base classes from which it derives properties and behaviors

# In[10]:


class Parent1:
    def method1(self):
        print("Method 1 from Parent 1")

class Parent2:
    def method2(self):
        print("Method 2 from Parent 2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method 3 from Child")

 
child_instance = Child() 
child_instance.method1()
child_instance.method2()
child_instance.method3()


# #Question 4

# Getter Method: A getter method is used to retrieve the value of a private attribute (an attribute with a leading underscore _) from a class. It provides controlled access to the attribute's value.
# 
# Setter Method: A setter method is used to modify the value of a private attribute while applying some validation or logic before assigning the new value.
# class Student:
#  
#    

# In[11]:


class Student:
    def __init__(self, name, age):
        self._name = name  
        self._age = age    

   
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

 
    def set_name(self, name):
        if len(name) > 1:
            self._name = name
        else:
            print("Name must have more than one character.")

 
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")
 
student = Student(name="Alice", age=20)

 
print("Name:", student.get_name())
print("Age:", student.get_age())

 
student.set_name("Bob")
student.set_age(25)
 
print("Name:", student.get_name())
print("Age:", student.get_age())


# #Question 5

# Method overriding in Python is a concept where a subclass provides a specific implementation for a method that is already defined in its superclass.

# In[ ]:


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

   
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

   
    def area(self):
        return 3.14 * self.radius ** 2
rectangle = Rectangle(width=5, height=3)
circle = Circle(radius=4)
 
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())

