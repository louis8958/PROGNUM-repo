#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from numpy import sin, cos, exp, pi
import numpy as np
import scipy.integrate

user_input = input("Enter a function: ")

def func_user(x):
    """Evaluates the user's string input safely."""
    try:
        return eval(user_input, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi, "np": np})
    except NameError as e:
        print(f"Error: Unknown function or variable! {e}")
        exit()
    except SyntaxError:
        print("Error: Unvalid Python syntax.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit()

# Integration calculation using quad function 
quad_integration = scipy.integrate.quad(func_user, 0, pi)
print(f'The integral of the function between 0 and pi is {quad_integration[0]} with error of {quad_integration[1]}')

# Integration calculation using Monte Carlo Method
def function(fun, x, a, b, n):
    return ((b - a)/n)*np.sum(fun)

a = 0
b = pi
n = 10000
x = np.random.uniform(a, b, n) 
y = np.array(func_user(x))

print(f'Using Monte Carlo method, the integral value is {function(y, x, a, b, n)}')

#To use these function to calculate the Area we have to input "x**4 +exp(cos(x)+sin(x))" in the user input to get the area, we get round 68 for both of the methods 

