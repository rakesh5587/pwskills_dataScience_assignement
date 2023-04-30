#!/usr/bin/env python
# coding: utf-8

# #question 1

# In[4]:


list=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list=sorted(list,key=lambda x:x[1])
sorted_list


# #question 2

# In[13]:


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_final=map(lambda x:x**2,l)
for i  in l_final:
    print(i, end=' ')


# #question 3

# In[25]:


li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_final=map(lambda x: str(x), li)
li1=[]
for i in l_final:
    li1.append(i)
tuple(li1 )   


# #question 4

# In[29]:


from functools import reduce
li=[]
for i in range(1,26):
    li.append(i)
reduce(lambda x,y:x*y, li)


# #question 5

# In[33]:


li=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
l_final=filter(lambda x:x%2==0 and x%3==0, li)
for i in l_final:
    print(i, end=" ")


# #question 6

# In[37]:


li=['python', 'php', 'aba', 'radar', 'level']
l_final=filter(lambda x:x==x[::-1], li)
for i in l_final:
    print(i, end=' ')


# In[ ]:




