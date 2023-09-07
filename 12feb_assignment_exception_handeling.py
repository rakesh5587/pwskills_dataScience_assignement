#!/usr/bin/env python
# coding: utf-8

# #Question 1

# Exceptions in Python:
# 
# Occur during program execution.
# Can be caught and handled using try and except.
# Examples: ZeroDivisionError, FileNotFoundError.
# 
# 
# Syntax Errors in Python:
# 
# Occur during code compilation before execution.
# Cannot be caught or handled with try and except.
# Examples: Typos, missing colons, indentation errors.

# #Question 2

# When an exception is not handled in Python, it will propagate up the call stack until it either reaches a suitable exception handler or, if not handled at all, it will cause the program to terminate

# In[1]:


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return f"Error: {e}"

result = divide(10, 0)
print("Result:", result)   


# #Question 3

# #In Python, the try, except, else, and finally statements are used to catch and handle exceptions

# In[4]:


try:
    result = 10 / 2  
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
else:
    print("No error occurred")


# In[5]:


try:
    result = 10 / 2  # This will not raise an exception
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed")


# #Question 4

# In[6]:


try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    print(f"The result of {num1} / {num2} is: {result}")
finally:
    print("Execution completed")


# The try block attempts to perform a division operation with user-inputted numbers.
# 
# 
# If the user enters a non-integer value, a ValueError exception is caught in the first except block, and it prints an error message.
# 
# 
# If the user tries to divide by zero, a ZeroDivisionError exception is caught in the second except block, and it prints an error message.
# 
# 
# If no exceptions occur during the execution of the try block, the else block is executed. It prints the result of the division.
# 
# 
# Finally, the finally block is always executed, regardless of whether an exception occurred or not. It indicates that the execution has completed.

# #Question 5

# They are derived from the base Exception class or one of its subclasses, and you define them to represent specific error conditions that are relevant to your application. 

# In[8]:


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

def custom_function(value):
    if value < 0:
        raise CustomError("Negative values are not allowed.")

try:
    custom_function(-5)
except CustomError as e:
    print(f"Custom error occurred: {e}")


# In[9]:


#Question 6


# In[10]:


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

def custom_function(value):
    if value < 0:
        raise CustomError("Negative values are not allowed.")

try:
    custom_function(-5)
except CustomError as e:
    print(f"Custom error occurred: {e}")


# In[ ]:




