#!/usr/bin/env python
# coding: utf-8

# #question 1
# 

# In[1]:


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']


# In[2]:


def product_of_numbers(lst):# first we have to create a falate list
    flat_lst = []
    for item in lst:
        if isinstance(item, (list, tuple, set)):
            flat_lst.extend(list(item))
        elif isinstance(item, dict):
            flat_lst.extend(item.values())
        else:
            flat_lst.append(item)

    product = 1
    for num in flat_lst:
        if isinstance(num, (int, float)):
            product *= num

    return product


# In[ ]:


product_of_numbers(list1)


# #question 2

# In[ ]:


def encrypt_message(message):
    encrypted = ""
    for char in message:
        if char.isalpha():
            encrypted += chr(219 - ord(char))
        elif char.isspace():
            encrypted += "$"
        else:
            encrypted += char
    return encrypted

