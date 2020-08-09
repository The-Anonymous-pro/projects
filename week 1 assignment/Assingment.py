#!/usr/bin/env python
# coding: utf-8

# ## ASSIGNMENT
# 
# **Tomiwa Emmanuel O. Am a python programmer and this script will be solving quadratic equations**.  A quadratic equation form is: **(ax² + bx + c = 0)**  which is solved using a quadratic formular:  **(-b +- √(b²-4ac))/2a**  where a, b, c are numbers and **a** is not equals to 0.
# 

# In[2]:


#First we import cmath module

import math

#Then we allow three(3) float inputs (a,b,c) for the quadratic equation

a= float(input("Enter a: "))
b= float(input("Enter b: "))
c= float(input("enter c: "))

#using the quadratic formular -b +- √(b² - 4ac)/2a we calculate x is (b²-4ac)

x= b**2 - 4*a*c

#since we have x ,we can now find the two solutions to the equation

first_sol = (-b - math.sqrt(x)) / (2*a)
second_sol = (-b + math.sqrt(x)) / (2*a)

#note that we already calculated for x, therefore the first and second solution need only to apply the quardratic formular.

print ( first_sol, second_sol )



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




