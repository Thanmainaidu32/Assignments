#!/usr/bin/env python
# coding: utf-8

# 1. Jupyter Notebook and Data Types
# Write a program in Jupyter Notebook to declare variables of different data types (integer, float, string, and boolean). Print each variable and its type.
# 

# In[ ]:


my_integer = 10
my_float = 20.5
my_string = "Hello, World!"
my_boolean = True
print("Integer value:", my_integer, "Type:", type(my_integer))
print("Float value:", my_float, "Type:", type(my_float))
print("String value:", my_string, "Type:", type(my_string))
print("Boolean value:", my_boolean, "Type:", type(my_boolean))


# Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples 
# 

# In[2]:


#list
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
first_fruit = fruits[0] 
third_fruit = fruits[2]  
print("First fruit:", first_fruit)
print("Third fruit:", third_fruit)


# In[3]:


#tuple
colors = ('red', 'blue', 'green', 'yellow', 'purple')
second_color = colors[1]  
fifth_color = colors[4] 
print("Second color:", second_color)
print("Fifth color:", fifth_color)


# In[6]:


# Dictionary 
ages = {'John': 25, 'Mary': 30, 'Sam': 22, 'Anna': 28, 'Tom': 32}
john_age = ages['John']  
anna_age = ages['Anna']  
print("John's age:", john_age)
print("Anna's age:", anna_age)


# Write a Python program that takes a student's marks in three subjects as input.
# If the average is greater than or equal to 90, print "Grade: A".
# If the average is between 80 and 89, print "Grade: B".
# If the average is between 70 and 79, print "Grade: C".
# Otherwise, print "Grade: Fail".
# 

# In[5]:


marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
average_marks = (marks1 + marks2 + marks3) / 3
if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
else:
    grade = "Fail"
print("Grade:", grade)


# In[ ]:




