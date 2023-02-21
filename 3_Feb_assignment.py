#!/usr/bin/env python
# coding: utf-8

# ##Question 1

# In[20]:


#def
li=[]
def fun():
    for i in range(0,26,1):
        c=2*i+1
        if c<=25:  
            li.append(c)
    return li
    


# In[21]:


fun()


# ##Question 2
# 

# In[23]:


if we want to pass any number of arguments in a function then we use *args and if we want to pass argumrnts in form of key and value pairs then we supply **kwargs
example:
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))



def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# ##Question 3

# In[24]:


Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.


# In[28]:


list =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
next_element=iter(list)
print(next(next_element))
print(next(next_element))
print(next(next_element))
print(next(next_element))
print(next(next_element))


# ##Question 4

# In[31]:


# a generator is a function that returns an iterator that produces a sequence of values when iterated over. yield keyword is used to create a generator function.
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


# ##Question 5

# In[ ]:


def primes():
    yield 2
    primes_so_far = [2]
    n = 3
    while n < 1000:
        is_prime = True
        for p in primes_so_far:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            yield n
            primes_so_far.append(n)
        n += 2

