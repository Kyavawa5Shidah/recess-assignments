#Group block of code
#There is need for code that is clean, reusable, maintainable
#def function_name():

def afternoon(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Attendees are close to 100")

#Callinug a function
afternoon("Shidah", "cassie")

#Arguments and parameters


#Modules
#A simple calc
def add( x , w):
    return(x + w)

def product(x, w):
    return(x * w)
"""
import module
y = module.product(2,7)
print(y)
"""

#Importing square root and factorial from the module math
from math import *

print(sqrt(16))
print(factorial(10))

#input and output in python
#input('prompt)

#Example of input

name = input("Enter your name: ")
print("My name is, "+ name)

#Example 2
number = int(input("Enter a value:"))
product = number * 10
print(product)

#multiple inputs in python
a, b, c = map(int, input("Enter the numbers:").split())
print("The values are:", end = "")
print(a, b, c)

#How to capture input from a tuple
m = (2,4,6,8)
print("Current tuple")
print(m)
print(type(m))

d = list(m)
d.append(int(input("Enter your new value: ")))
m = tuple(d)
print("updated tuple")
print(m)

#Example
mylist = list(map(int, input("Enter the list values:").split()))
myset = set(map(int, input("Enter the set values:").split()))
print(mylist)
print(type(mylist))
print(myset)
print(type(myset))