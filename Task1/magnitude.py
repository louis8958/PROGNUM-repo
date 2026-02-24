#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Magnitude data
m = float(input(' The apparent Magnitude is '))
M = float(input(' The absolute Magnitude is '))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164

print (f"The distance is {d:g} ly")


# In[ ]:




