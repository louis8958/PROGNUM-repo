#!/usr/bin/env python
# coding: utf-8

# Answers for Week 1
# Name : Louis Suberbere
# Username : lbjsuberbere
# Student No : S6080081
# Group : AS2

# Question 1.2

# In[6]:


x = 22/7


# $$y=\frac{sin(x)}{x}$$

# In[7]:


pi = 22/7 # Processed on Jupyter Hub


# ![dolphin.png](attachment:38852521-409b-4c54-9bad-10a7711be2ef.png)

# Question 1.3

# In[8]:


x = 6
x *= 5
x *= 4
x *= 3
x *= 2
print (x)


# Question 1.4

# In[10]:


from astropy.constants import c, h 
freq = 2.42 * 10e28 #in Hz
Lambda = 1 / freq
E = (h * c)/Lambda 
print (E)


# Question 1.5

# In[14]:


from astropy.constants import G
m_1 = 7.342 * 10e22 # in kg 
m_2 = 5.9722 * 10e24 # in kg
r = 385000.6 * 10e3 #in m
F = (G* m_1 * m_2)/(r**2)
print (F)


# Question 1.7

# In[16]:


x1 = 10
x2 = 22/7
print(x1, end="")
print(x2, end="")


# Explanation : This end zithout anything in it allows to print both x1 and x2 on the same line, that is without a new line being started after printing the first value

# Question 1.9

# [lbjsuberbere@jupyterhub1 Downloads]$ echo $SHELL
# /bin/bash
# [lbjsuberbere@jupyterhub1 Downloads]$ echo $SHELL
# /bin/bash
# [lbjsuberbere@jupyterhub1 Downloads]$ ls
# coursework_week1.ipynb  dolphin.png  thinkpython2.pdf  Untitled.ipynb
# [lbjsuberbere@jupyterhub1 Downloads]$ ls-rtl
# bash: ls-rtl: command not found...
# [lbjsuberbere@jupyterhub1 Downloads]$ ls -rtl
# total 896
# -rw-r--r-- 1 lbjsuberbere users    624 Feb 10 16:03 Untitled.ipynb
# -rw-r--r-- 1 lbjsuberbere users   7252 Feb 10 16:05 dolphin.png
# -rw-r--r-- 1 lbjsuberbere users 814210 Feb 10 16:22 thinkpython2.pdf
# -rw-r--r-- 1 lbjsuberbere users  88481 Feb 10 17:22 coursework_week1.ipynb
# [lbjsuberbere@jupyterhub1 Downloads]$ man ls
# [lbjsuberbere@jupyterhub1 Downloads]$ a.txt
# bash: a.txt: command not found...
# [lbjsuberbere@jupyterhub1 Downloads]$ a .txt
# bash: a: command not found...
# [lbjsuberbere@jupyterhub1 Downloads]$ touch a.txt
# [lbjsuberbere@jupyterhub1 Downloads]$ cp a.txt b.txt
# [lbjsuberbere@jupyterhub1 Downloads]$ mv b.txt c.txt
# [lbjsuberbere@jupyterhub1 Downloads]$ mkdir PROGNUM
# [lbjsuberbere@jupyterhub1 Downloads]$ cd PROGNUM
# [lbjsuberbere@jupyterhub1 PROGNUM]$ cp ../../a.txt .
# cp: cannot stat '../../a.txt': No such file or directory
# [lbjsuberbere@jupyterhub1 PROGNUM]$ pwd
# /Users/users/lbjsuberbere/Downloads/PROGNUM
# [lbjsuberbere@jupyterhub1 PROGNUM]$ cd Task1
# bash: cd: Task1: No such file or directory
# [lbjsuberbere@jupyterhub1 PROGNUM]$ ls
# 'Task 1'
# [lbjsuberbere@jupyterhub1 PROGNUM]$ mv Task\ 1/ Task1
# [lbjsuberbere@jupyterhub1 PROGNUM]$ ls
# Task1
# [lbjsuberbere@jupyterhub1 PROGNUM]$ cd Task1
# [lbjsuberbere@jupyterhub1 Task1]$ cp ../../a.txt .
# [lbjsuberbere@jupyterhub1 Task1]$ cd ../../
# [lbjsuberbere@jupyterhub1 Downloads]$ ls
# a.txt  coursework_week1.ipynb  c.txt  dolphin.png  PROGNUM  thinkpython2.pdf  Untitled.ipynb
# [lbjsuberbere@jupyterhub1 Downloads]$ cd ../../ ls
# bash: cd: too many arguments
# [lbjsuberbere@jupyterhub1 Downloads]$ rm a.txt
# [lbjsuberbere@jupyterhub1 Downloads]$ 


#Question 1.15
#1) output of pwd is : /Users/users/vogelman/Downloads/
#2) the . corresponds to the current directory and the .. is for the one upward that is volgelman

#Question 1.16
#cd ~/Desktop

#Question 1.19
#1)This command lists all files in the current directory that meet the following criteria: The filename must contain at least one digit (0-9) somewhere in the name and the filename must end with either a .c or a .o extension so it basically prints all the corresponding files
#2) the square brackets are a wildcard used to match exactly one character from a specific set or range of character
#3)It lists files containing a digit that end specifically with the exact extension .co so less files are printed