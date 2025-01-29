#!/usr/bin/env python
# coding: utf-8

# 1. Jupyter Notebook and Data Types
# Write a program in Jupyter Notebook to declare variables of different data types (integer, float, string, and boolean). Print each variable and its type.
# 

# In[1]:


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


# In[4]:


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

# In[ ]:


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


# ##DAY=4
# Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n
# 

# In[ ]:


n = int(input("Enter a positive integer: "))
sum_even = 0
for i in range(2, n + 1, 2):
    sum_even += i
print("Sum of all even numbers between 1 and", n, "is:", sum_even)


# ##DAY=5
# 1)Write a Python program that performs the following tasks:
# 
# 1. Ask the user to enter a positive integer `n`.
# 2. Use a `for` loop to print all numbers from `1` to `n` on separate lines.
# 3. Use a `while` loop to calculate the sum of all numbers from `1` to `n` and print the result.
# 
# 
# 2)Write a Python program that includes a user-defined function to perform the following tasks:
# 
# 1. Define a function named calculate_square that takes a single argument `n` and returns the square of `n`.
# 2. In the main program, ask the user to input a positive integer.
# 3. Call the calculate_square function with the user-provided number and display the result.
# 
# 
# 
# 

# In[ ]:


# Get a positive integer from the user
n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i)
i = 1
while i <= n:
    total_sum += i
    i += 1
print("Sum of all numbers from 1 to", n, "is:", total_sum)


# In[ ]:


# Define a function to calculate the square of a number
def calculate_square(n):
    return n * n
number = int(input("Enter a positive integer: "))
square = calculate_square(number)
print("The square of", number, "is:", square)


# 

# In[ ]:





# In[ ]:




