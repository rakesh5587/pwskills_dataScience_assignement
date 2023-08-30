#!/usr/bin/env python
# coding: utf-8

# Question 1
# 

# In most programming languages, including Python, the function used to open a file is usually named open()
# here are some modes are defiend
# #Reading a file
# with open('example.txt', 'r') as file:
#     content = file.read()
# 
# #Writing to a file
# with open('output.txt', 'w') as file:
#     file.write('Hello, world!') # it will trunckate the existing file 
# 
# #Appending to a file
# with open('data.txt', 'a') as file:
#     file.write('New data\n') # it will not truncate the file
# 
# #Binary read and write mode
# with open('image.png', 'rb') as file:
#     image_data = file.read()
# 

# Question 2

# The close() function is used to explicitly close a file that has been opened using the open() function.
# 
# its importtant to close a file because 
# 1. resourse management 
# 2. data integrity
# 3. file locking 
# 4. operating system limits 
# 5. probability 

# Question 3
# 

# In[1]:


# Open the file in write mode
with open('data_scientist.txt', 'w') as file:
    file.write('I want to become a Data Scientist')

# Reading the content of the file
with open('data_scientist.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)


# Question 4

# 1.The read() method is used to read the entire content of a file as a single string. It reads from the current file position up to the end of the file. 
# 2.The readline() method is used to read a single line from the file. It reads from the current file position up to and including the newline character (\n).
# 3.The readlines() method is used to read all lines from the file and return them as a list of strings. Each line is a separate element in the list.

# Question 5

# Using the with statement is considered best practice because it reduces the risk of leaving files open due to errors or exceptions in your code.

# Question 6

# 1. The write() method is used to write a string of characters to a file. It adds the provided string to the end of the file's current content, starting from the current file position.
# 2. writelines() method is used to write a list of strings to a file. Each string in the list corresponds to a line that will be written to the file.
