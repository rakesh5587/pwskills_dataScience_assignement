#!/usr/bin/env python
# coding: utf-8

# #question 1

# In[ ]:


import re

def check_password(password):
    if len(password) != 10:
        return "Invalid Password"
    else:
        upper_count = 0
        lower_count = 0
        digit_count = 0
        special_count = 0
        for char in password:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char.isdigit():
                digit_count += 1
            elif re.match(r'[^\w\s]', char):
                special_count += 1
        if upper_count >= 2 and lower_count >= 2 and digit_count >= 1 and special_count >= 3:
            return "Valid Password"
        else:
            return "Invalid Password"

