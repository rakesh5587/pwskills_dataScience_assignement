#!/usr/bin/env python
# coding: utf-8

# ##Question 1

# In[5]:


per=float(input("enter your percentage: "))
if per>90:
    print("A")
elif per>80 and per<=90:
    print("B")
elif per>=60 and per<=80:
    print("B")
else:
    print("D")


# ##Question 2

# In[14]:


cost=float(input("enter the cost"))
if cost>100000:
    print("tax will be: ",cost*.15)
elif cost>50000 and cost<=100000:
    print("tax will be: ",cost*.10)
else:
    print("tax will be ",cost*.05)


# In[ ]:


city_dict={"Delhi":"Red fort",'Agra':"Taj mahal",'Jaipur':'Jal mahal'}
city=input("enter your city")
if city in city_dict.keys():
    print("Monument in your city is :", city_dict[city])


# ##Question 4

# In[ ]:


# Question is not clear


# ##Question 5
# 

# In[ ]:


Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed
example:
    count = 0
while (count < 3):
    count = count + 1
    print("Hello word")


# ##Question 7 & 8

# In[25]:


n=10
while n>0:
    print(n, end=' ')
    n=n-1
    


# In[ ]:




