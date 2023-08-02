#used to store data values in key values pairs
#Dictionaries are ordered, changeabl but do not allow duplicates
#Dicts can have items of any data type

mydict = {
    "phone": "iphone",
    "iphonemodel": "iphone15",
    "year": 2023
}
print(mydict)

#length of a dictionary
print(len(mydict))


#datatype
print(type(mydict))

#Access dictionary items
z = mydict["year"]
print(z)
y = mydict.get("iphonemodel")
print(y)

#Keys
w = mydict.keys()
print(w)

#numbers
# integers, floats, complex
w = 10 #int
r = 3.9 #float
s = 2j #complex

print(type(w))
print(type(r))
print(type(s))

#integer
a = 2
b = 2345678
c = -2344

print(type(a))
print(type(b))
print(type(c))

#Floats
x = 2.34
y = 2.7889900
z = -34.7899

print(type(x))
print(type(y))
print(type(z))

#Complex numbers
h = 5 + 12j
t = 7j
m = -6j

print(type(h))
print(type(t))
print(type(m))

#type conversions
w = 10 #int
r = 3.9 #float
s = 2j #complex
 
 #convert from int to complex
d = complex (w)
print(d)
print(type(d))

#convert from int to float
#convert from float to complex

#Strings
#print("Afternoon")
#print('Afternoon')

#Assign string to a variable
w = "Afternoon"
#print(w)
#Multine strings
q = """I am offering BSSE
Currently doing recess"""
print(q)

# strings as arrays
a = "Afternoon"
print(a[0])

#How to modify strings
b = "Afternoon"
print(b.lower())
print(b.upper())

# Remove white space
c = " After noon"
print(c.strip())

#String concatenation
d = "Afternoon"
e = "class"
w = c + d
print(w)

#Booleans
#These evaluate to a true or false
print(20 < 10)
print(30 == 40)
print(30 > 10)
print(bool(15))

r = "Livingstone"
z = 30

print(bool(r))
print(bool(z))

#Assignment
#Exercise One: use the values () method to return a list of all values in the dictionary
mydict2 = {
    "name": "shidah",
    "age":20,
    "year": 2023
}
x = list(mydict2.values())
print(x)

#Exercise Two: to check if a key does exit in your dictionary
mydict2 = {
    "name": "shidah",
    "age":20,
    "year": 2023
}
key_to_check = "age"

if key_to_check in mydict2:
    print("Key exists!")
else:
    print("Key does not exist!")

#Exercise Three: Give an example on how to change dictionary items, how to update
students = {
    "John": 20,
    "Emily": 18,
    "Michael": 19
}
#changing Emily's age to 19
students["Emily"] = 19
#updating the dictionary
students["Sarah"] = 21
print(students)

#Exercise Four :Give an example on how to add dictionary items, how to remove dictionary items
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78
}
# Adding a new item to the dictionary
student_scores["Sarah"] = 95
print(student_scores)
# Removing an item from the dictionary
del student_scores["John"]
print(student_scores)

#Exercise Five: Give an example on how you can loop through a dictionary and also how to nest dictionaries
student_scores = {
    "John": 85,
    "Emily": 92,
    "Michael": 78
}
# Loop through the dictionary
for student, score in student_scores.items():
    print(f"{student} scored {score}")
#Nesting dictionaries
students = {
    "John": {
        "age": 20,
        "score": 85
    },
    "Emily": {
        "age": 18,
        "score": 92
    },
    "Michael": {
        "age": 19,
        "score": 78
    }
}
# Accessing nested dictionary values
for student, details in students.items():
    print(f"{student}: Age: {details['age']}, Score: {details['score']}")

#Exercise Six: Determine the length of a string using the len() function
text = "Hello world"
length = len(text)
print(length)

#Exercise Seven: Give an example Iterate through each character in a string using a for loop
text = "Hello"
# Iterate through each character in the string
for char in text:
    print(char)
    
#Exercise Eight: Give an example Slice a string to extract specific portions of it
text = "Hello world"
#slicing the string
sliced_text = text[7:12]
print(sliced_text)

#Exercise Nine: Perform arithmetic operations with numbers and print the results
a = 10
b = 5

sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b
# Print the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)

#Exercise Ten: Use boolean values and conditions to control program flow
a = 10
b = 5

is_greater = a > b
is_equal = a == b
# Conditional statements
if is_greater:
    print("a is greater than b")
elif is_equal:
    print("a is equal to b")
else:
    print("a is less than b")
