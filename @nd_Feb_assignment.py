#!/usr/bin/env python
# coding: utf-8

# ##Question 1

# In[1]:


They are indexed
Tuples are ordered
These are immutable
They can contain duplicate items


# ##Question 2

# In[2]:


The count() method of Tuple returns the number of times the given element appears in the tuple
example:
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)=3
The Index() method returns the first occurrence of the given element from the tuple.
example:
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)=3
Tuple have only two methos just because Tuple is immutable


# ##Question 3

# In[8]:


# Set
# example:
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
s=set(li)
s


# ##Question 4

# update() adds all missing elements to the set on which it is called
# union() creates a new set.

# In[13]:


a={1,2,3,4,5,0}
b={6,3,4,7,8}
c=a.update(b)# b will remain same 
a


# In[14]:


a.union(b)# it will create a new set and a as well as b will be remain same 


# ##Question 5

# In[15]:


Dictionary is also a collection of data similar like a list in which values will be stored in the form of key: value paires.
dictionary is also iterable and ordered formate
exmple:
    {"rakesh":1,"vikssh":2,"ramesh":3,"rajesh":4,"ajai":6}


# ##Question 6

# In[16]:


{1: {'name': 'John', 'age': '27', 'sex': 'Male'},2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}


# ##Question 7

# In[30]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}


# In[31]:


dict1.setdefault(" ","machine learning")


# In[32]:


dict1


# ##Question 8

# In[33]:


dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}


# In[39]:


dict1.keys()


# In[40]:


dict1.values()


# In[42]:


dict1.items()


# In[ ]:




