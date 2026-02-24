#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Y = float(input("The year is "))
M = float(input("The month is "))
D = float(input("The day is "))

JD = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5
print(f'The Julian Date is {JD}')

