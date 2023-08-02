#Exception handling
"""
Exception handling in Python allows you to handle runtime errors or exceptions that may occur 
during the execution of your program. 
It helps you gracefully handle errors and prevents your program from crashing. 

Try-Except block: The try block is used to enclose the code that might raise an exception, 
while the except block is used to handle the exception if it occurs.
"""
try:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

#Handling Multiple Exceptions: You can handle multiple exceptions by including multiple
#except blocks after the try block. Each except block specifies the type of exception it can handle.
try:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print("Error:", str(e))

#Handling Multiple Exceptions Together: You can handle multiple exceptions together by 
#using a single except block and specifying multiple exception types as a tuple.
try:
    
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except (ZeroDivisionError, ValueError) as e:
    print("Error:", str(e))

#Handling Any Exception: You can handle any type of exception using a generic except block. 
#However, it's generally recommended to handle specific exceptions whenever possible.
try:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except Exception as e:
    print("Error:", str(e))

#Finally Block: The finally block is used to specify code that should always be executed, 
#regardless of whether an exception occurred or not.
try:
    
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("Program execution completed.")

#Raising Exceptions: You can raise exceptions manually using the raise statement to 
#indicate that an error condition has occurred.

def calculate_age(year):
    current_year = 2023
    if year > current_year:
        raise ValueError("Invalid year.")
    age = current_year - year
    return age

try:
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    print("Your age:", age)
except ValueError as e:
    print("Error:", str(e))

#File handling
"""
File handling in Python allows you to read from and write to files on your computer. 
It provides a convenient way to work with data stored in files. 
Opening a File: To work with a file, you need to open it using the open() function. 
You need to provide the file path and specify the mode (read, write, append, etc.) in
which you want to open the file. 
"""

#Reading from a File: Once you have opened a file, you can read its contents using various methods.
#The most common method is read(), which reads the entire contents of the file as a string
file = open("example.txt", "r")
contents = file.read()

# Print the contents
print(contents)

# Close the file
file.close()

#Writing to a File: To write data to a file, you need to open it in write mode using the open() 
#function. You can use the write() method to write data to the file.
# Open a file in write mode
file = open("example.txt", "w")

# Write data to the file
file.write("Hello, World!")

# Close the file
file.close()

#Appending to a File: If you want to add new data to an existing file without overwriting its 
#contents, you can open the file in append mode using the open() function
# Open a file in append mode
file = open("example.txt", "a")

# Append data to the file
file.write("Appending new data.")

# Close the file
file.close()

"""
Closing a File: After you finish working with a file, it's important to close it using the close()
 method. This ensures that any changes made to the file are saved and the system resources
 are freed up. Alternatively, you can use the with statement, which automatically 
takes care of closing the file for you.
"""
# Using the with statement
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
# The file is automatically closed at the end of the with block

#Exception Handling in File Handling
try:
    # Open a file in read mode
    file = open("example.txt", "r")

    # Read the contents of the file
    contents = file.read()

    # Print the contents
    print(contents)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", str(e))
finally:
    # Close the file
    file.close()
