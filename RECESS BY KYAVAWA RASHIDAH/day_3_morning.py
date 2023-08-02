

#Examples of arithmetic operators
#Addition
x = 50 + 45
print(x)
#subtraction
y = 50 - 45
print(y)
#Multiplication
z = 50 * 45
print(z)
#division
a = 50 / 5
print(a)
#divide
b = 50 // 5
print(b)
# modulus
c = 100 % 3
print(c)
#exponentiation
d = 4 ** 8
print(d)

#Examples of comparison operators
#comparison operators
a = 30
b = 10

# Greater than
if a > b:
    print('a is greater than b')
    print(a > b)
# Less than
if a < b:
    print('a is less than b')
    print(a < b)
# greater than or equal to
if a >= b:
    print('a is greater than or equal to b')
    print(a >= b)
# less than or equal to
if a <= b:
    print('a is less than or equal to b')
    print(a <= b)
#equal to
if a == b:
    print('a is equal to b')
    print(a == b)
#Not equal to
if a != b:
    print('a is not equal to b')
    print(a != b)
# less than or equal to
print(a <= b)
# equal to
print( a == b)

#Examples of logical operators
#Logical operators
m = True
n = False

#Logical AND
print(m and n)
#Logical OR
print(m or n)
#Logical NOT
print(not m)
print(not n)

# Examples of Assignment operator
#compound assignment operator
p = 8

#Add and assign
p += 8
print(p)
#Subtract and assign
l = 18
l -= 8
print(l)
#multiply and assign
h = 23
h *= 3
print(h)
# divide and assign
g = 45
g /= 3
print(g)
#modulus and assign
f = 19
f %= 3
print(f)
#exponentation and assign
e = 2
e **= 4
print(e)

#Examples of memebership assignment operators
cars =['Jeep', 'Telsa', 'BMW', 'Roll Royce']
if 'Jeep' in cars:
    print('Jeep is in the list')
    print('Telsa' in cars)
    print('Toyota' in cars)

#identity operators
x = 10
y = 10
#is operator
print(x is y)
print(x is not y)
print( x == y)
print( x != y)
print( x < y)
print( x <= y)

#List
# is not operator
z = [1,2,3,4,5]
w = [1,2,3,4,5]
print(z is not w)

#Bitwise opeartors
"""
They are used to perform operations on individual bits in of binary numbers.
Bitwise AND (&): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR (|): Performs a bitwise OR operation between the corresponding bits of two integers
Bitwise XOR(^): Performs a bitwise XOR operation
Bitwise NOT(-): Performs a bitwise NOT operation between the corresponding bits of two integers
Bitwise left shift (<<): Performs a bitwise left shift operation 
Bitwise right shift(>>): Performs a bitwise right shift operation 
"""
#Examples of Bitwise operations
a = 10
b = 30

#Bitwise AND operation
result_and = a & b
print(result_and)
#Bitwise OR operation
result_or = a | b
print(result_or)
#Bitwise XOR operation
result_xor = a ^ b
print(result_xor)
#Bitwise NOT operation
result_not = a - b
print(result_not)
#Bitwise left shift
result_leftshift = a << b
print(result_leftshift)
#Bitwise rught shift
result_rightshift = a >> b
print(result_rightshift)

#Example
#Create a simple calculator function to calculate(add, subtract, multiply and divide)
def add(a, b):
  return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def main():
    print('Rashidah simple calculator')
    number1 = float(input("Enter your first number:"))
    number2 = float(input("Enter your second number:"))
    operator = input("Enter the operator (+, -, *, /):")

    if operator == '+':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)
    elif operator == '*':
        result = multiply(number1, number2)
    elif operator == '/':
        result = divide(number1, number2)
    else:
        print('Invalid operator')
        return
    print("the result is", result)

if __name__ == '__main__':
    main()

#Exercise
#tkinter learn
#Assignment create a simple calculator program with a GUI interface. 
#Make the title of the calculator program window with your name 

import tkinter as tk

# Function to perform calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Creating the main window
window = tk.Tk()
window.title(" Kyavawa Rashidah simple calculator")

# Creating the entry widget to display and input values
entry = tk.Entry(window, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating the buttons for numbers and operations
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Adding the buttons to the window
row = 1
col = 0

for button in buttons:
    btn = tk.Button(window, text=button, width=5, height=2, font=("Arial", 12), command=lambda text=button: entry.insert(tk.END, text))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1

    # Move to the next row after every 4 buttons
    if col > 3:
        col = 0
        row += 1

# Creating the equals button for calculation
equals_btn = tk.Button(window, text="=", width=5, height=2, font=("Arial", 12), command=calculate)
equals_btn.grid(row=row, column=col, padx=5, pady=5)

# Running the main window
window.mainloop()

    