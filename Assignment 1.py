#!/usr/bin/env python
# coding: utf-8

# Q1. Create one variable containing following type of data:
# (i) string
# (ii) list
# (iii) float
# (iv) tuple

# In[1]:


a='abc'

b=[1,2,3,'abc',3.14,True]

c=3.14

d=(2,3,4,5)


# Q2. Given are some following variables containing data:
# (i) var1 = ' '
# (ii) var2 = '[DS,ML,Python]'
# (iii) var3 = ['DS','ML','Python' ]
# (iv) var4 = 1

# In[2]:


var1 = ''
print(type(var1))

var2 = '[DS,ML,Python]'
print(type(var2))

var3 = ['DS','ML','Python' ]
print(type(var3))

var4 = 1
print(type(var4))


# Q3. Explain the use of the following operators using an example:
# (i) /
# (ii) %
# (iii) //
# (iv) **

# In[3]:


6/3 # divide 6 by 3

6%3 # gives remainder

6//3 # gives quotient

6**3 # 6 to the power 3


# Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

# In[4]:


l=[1,2,3,False,'xyz','abc',1.11,93.2,3.14,True]
for i in l:
    print(i,'=',type(i))


# Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

# In[5]:


def count_divisions(A, B):
    count = 0
    while A % B == 0:
        A /= B
        count += 1
    return count

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))

divisions = count_divisions(A, B)

if divisions > 0:
    print(f"{A} is purely divisible by {B} and can be divided {divisions} times.")
else:
    print(f"{A} is not purely divisible by {B}.")

