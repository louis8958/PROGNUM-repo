#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import *
a = float(input("The value of a is "))
b = float(input("The value of b is "))
c = float(input("The value of c is "))
D = b**2 -4*a*c
if D > 0 : 
    x_1 = (-b + sqrt(D)) / 2*a
    x_2 = (-b - sqrt(D)) / 2*a
    print (f"The roots of the function are {x_1} and {x_2}")
elif D == 0 :
    x = -b/2*a
    print (f"The root of the function is  {x}")
else : 
    print ("The function has no real roots")

