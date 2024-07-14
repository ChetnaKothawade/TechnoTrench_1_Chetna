#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(" Simple Calcuator")
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))

print("1. Addition \n")
print("2. Subtraction \n")
print("3. Multiplication \n")
print("4. Division \n")
choice = int(input("Enter your choice number from 1-4:"))

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)
else:
    print("Invalid Choice")

