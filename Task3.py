#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string
print("Sales Forecasting Password Generator")
def main():
    length=int(input("Enter the string length:"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolD=string.punctuation
    combine=lowerD+upperD+digitD+symbolD
    x=random.sample(combine, length)
    password="".join(x)
    print(password)
main()


# In[ ]:




