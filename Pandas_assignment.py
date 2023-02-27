#!/usr/bin/env python
# coding: utf-8

# ##Question 1

# In[1]:


import pandas as pd
data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)


# In[2]:


series


# ##Question 2

# In[3]:


import pandas as pd
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_series = pd.Series(my_list)
my_series


# ##Question 3

# In[5]:


data={"name":["Alice", "Bob", "Clair3"],
     "age":[25,30,27],
     "Gander":["Female","Male","Female"]}
import pandas as pd


# In[6]:


df=pd.DataFrame(data)


# In[7]:


df


# ##Question 4

# In[8]:


# In Pandas, a DataFrame is a two-dimensional tabular data structure that contains rows and columns of data. It can be thought of as a spreadsheet or a SQL table. Each column in a DataFrame is a Pandas Series.

# A Pandas Series, on the other hand, is a one-dimensional array-like data structure that contains a single sequence of data values. It can be thought of as a column in a spreadsheet or a SQL table.

# Here's an example that demonstrates the difference between a Pandas DataFrame and a Pandas Series:


# In[9]:


data={"name":["Alice", "Bob", "Clair3"],
     "age":[25,30,27],
     "Gander":["Female","Male","Female"]}
import pandas as pd
df=pd.DataFrame(data)
df


# In[10]:


#df is a data frame 


# In[12]:


ser=df["name"]


# In[13]:


type(ser)


# In[14]:


#ser is a series


# ##Question 4

# In[15]:



head() and tail()


# ##Question 5

# In[16]:


# Both Series and DataFrame are mutable in nature


# ##Question 6

# In[ ]:


import pandas as pd
name = pd.Series(['Alice', 'Bob', 'Charlie'])
age = pd.Series([25, 30, 35])
gender = pd.Series(['F', 'M', 'M'])
df = pd.DataFrame({'name': name, 'age': age, 'gender': gender})
 
 

