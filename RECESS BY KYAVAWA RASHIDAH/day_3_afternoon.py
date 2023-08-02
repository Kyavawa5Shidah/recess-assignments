#Exercise1 (Lists)
#Create a list with 5 items(names of people) and write a python program to output the second item
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
second_name = names[1]
print(second_name)

#Write a python program to change the value of the first item to a new value
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_value = "Alex" 
names[0] = new_value
print(names)

# Write a python program to add a sixth item to the list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_item = "Frank" 
names.append(new_item)
print(names)

#Write a python program to add "Bathel" as the third item in your list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_item = "Bathel"  
position = 2  # The index where you want to insert the new item
names.insert(position, new_item)
print(names)

#Write a python program to remove the fourth item from the list
names = ["Alice", "Bob", "Bathel", "Charlie", "David", "Eve"]
position = 3  # The index of the item you want to remove
removed_item = names.pop(position)
print("Removed item:", removed_item)
print("Updated list:", names)

#Use negative indexing to print the last in your list
names = ['Alice', 'Bob', 'Bathel', 'David', 'Eve']
last_item = names[-1]
print(last_item)

#Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
third_to_fifth_items = items[2:5]
print(third_to_fifth_items)

#Write a list of countries and make a copy of it.
countries = ["United States", "Canada", "United Kingdom", "Germany", "France"]
countries_copy = countries.copy()
print("Original list of countries:", countries)
print("Copy of the list of countries:", countries_copy)

# Write a python program to loop through the list of countries
countries = ["United States", "Canada", "United Kingdom", "Germany", "France"]
for country in countries:
    print(country)

# Write a list of animal names and sort them in both descending and ascending order
animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Monkey"]

# Sort in ascending order
ascending_order = sorted(animals)

# Sort in descending order
descending_order = sorted(animals, reverse=True)
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

#. Using the list above, write a python program to output only animal names with the letter 
#‘a’ in them
animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Monkey"]

# Filter animal names with the letter 'a'
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animal names with 'a':", animals_with_a)

#Write two lists, one containing your first names and the other your second names. Join 
#the two lists.
first_names = ["John", "Jane", "Michael", "Emily"]
last_names = ["Doe", "Smith", "Johnson", "Williams"]

full_names = [first + " " + last for first, last in zip(first_names, last_names)]
print("Full Names:", full_names)

#Exercise 2(Tuples)
"""
 Consider the tuple below;
x = (“samsung”, “iphone”, “tecno”, “redmi”)
Write a python program to output your favorite phone brand
"""
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = "iPhone"

if favorite_brand in x:
    print("Your favorite phone brand is", favorite_brand)
else:
    print("Your favorite phone brand is not in the tuple")

#Use negative indexing to print the 2nd last item in your tuple. 
x = ("samsung", "iphone", "tecno", "redmi")

second_last_item = x[-2]
print("The second-to-last item is:", second_last_item)

#Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")

# Convert the tuple to a list
x_list = list(x)

# Update "iphone" to "itel" in the list
x_list[x_list.index("iphone")] = "itel"

# Convert the list back to a tuple (optional)
x_updated = tuple(x_list)
print("Updated tuple:", x_updated)

#Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
new_element = "Huawei"

# Create a new tuple by concatenating the original tuple and the new element
x_updated = x + (new_element,)
print("Updated tuple:", x_updated)

#Write a python program to loop through the tuple above.
x = ("samsung", "iphone", "tecno", "redmi")
for item in x:
    print(item)

# Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")

# Create a new tuple without the first item
x_updated = x[1:]
print("Updated tuple:", x_updated)

# Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("Tuple of cities in Uganda:", cities)

# Write a python program to unpack your tuple.
x = ("samsung", "iphone", "tecno", "redmi")

# Unpack the tuple into separate variables
item1, item2, item3, item4 = x
# Print the unpacked variables
print("Unpacked variables:")
print("Item 1:", item1)
print("Item 2:", item2)
print("Item 3:", item3)
print("Item 4:", item4)

# Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
# Print the 2nd, 3rd, and 4th cities using index range
print("2nd city:", cities[1])
print("3rd city:", cities[2])
print("4th city:", cities[3])

# Write two tuples, one containing your first names and the other your second names. Join 
#the two tuples.
first_names = ("John", "Jane", "Michael", "Emily")
last_names = ("Doe", "Smith", "Johnson", "Williams")

full_names = first_names + last_names
print("Full Names:", full_names)

# Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")

multiplied_colors = colors * 3
print("Multiplied colors:", multiplied_colors)

#Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)

#Exercise 3(Sets)
#Use the set() constructor to create a set of 3 of your favorite beverages.
favorite_beverages = set(["coffee", "tea", "juice"])

print("Favorite beverages:", favorite_beverages)

#Use the correct method to add 2 more items to the beverages set.
favorite_beverages = {"coffee", "tea", "juice"}

# Using the add() method to add a single item
favorite_beverages.add("water")

# Using the update() method to add multiple items
favorite_beverages.update(["soda", "smoothie"])

print("Updated favorite beverages:", favorite_beverages)

# Given the set below;
"""
mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
Check if microwave is present in the set.
"""
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

# Write a python program to remove “kettle” from the set above.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

# Using the remove() method
mySet.remove("kettle")

# Using the discard() method
mySet.discard("kettle")

print("Updated set:", mySet)

# Write a python program to loop through the set above
mySet = {"oven", "kettle", "microwave", "refrigerator"}

print("Looping through the set:")
for item in mySet:
    print(item)

# Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {"apple", "banana", "orange", "grape"}
myList = ["kiwi", "mango"]

print("Set before adding list elements:", mySet)

# Add elements from the list to the set
mySet.update(myList)

print("Set after adding list elements:", mySet)

# Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35, 40}
first_names = {"John", "Jane", "Michael", "Emily"}

joined_set = ages.union(first_names)

print("Joined Set:", joined_set)

#Exercise 4(Strings)
#Declare two variables, an integer and a string and use the correct method to concatenate the two variables
my_integer = 10
my_string = "Hello"
concatenated_string = str(my_integer) + my_string
print("Concatenated String:", concatenated_string)

#Consider the example below;
"""
txt = “ Hello, Uganda! ”
Output the string without spaces at the beginning, in the middle and at the end.
"""
txt = " Hello, Uganda! "
output = txt.strip()
print("Output string:", output)

# Write a python program to convert the value of ‘txt’ to uppercase
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print("Uppercase string:", uppercase_txt)

# Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = "Hello, Uganda!"
updated_txt = txt.replace('U', 'V')
print("Updated string:", updated_txt)

# Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
substring = y[1:4]
print("Substring:", substring)

#The piece of code below will give an error when output;x = “All “Data Scientists” are cool!” Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)

#Exercise 5(Dictionaries)
# With reference to the dictionary below, write a python program to print the value of the shoe size.
""" 
Add this dictionary to your .py file
Shoes = {
“brand” : “Nick”,
“color” : “black”,
“size” : 40
}
"""
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print("Shoe size:", shoe_size)

#Write a python program to change the value “Nick” to “Adidas”
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["brand"] = "Adidas"
print("Modified Shoes dictionary:", Shoes)

#Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["type"] = "sneakers"
print("Modified Shoes dictionary:", Shoes)

#Write a python program to return a list of all the keys in the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
keys_list = list(Shoes.keys())
print("List of keys:", keys_list)

#Write a python program to return a list of all the values in the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
values_list = list(Shoes.values())
print("List of values:", values_list)

#Check if the key “size” exists in the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")

#Write a python program to loop through the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
for key, value in Shoes.items():
    print(key, ":", value)

# Write a python program to remove “color” from the dictionary.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
del Shoes["color"]
print("Modified Shoes dictionary:", Shoes)

#Write a python program to empty the dictionary above.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes.clear()
print("Empty Shoes dictionary:", Shoes)

#Write a dictionary of your choice and make a copy of it.
# Creating the original dictionary
original_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Making a copy of the original dictionary
copied_dict = dict(original_dict)

# Modifying the copied dictionary
copied_dict["age"] = 35

# Printing both dictionaries
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

#Write a python program to show nested dictiionaries
student = {
    "name": "John Doe",
    "age": 20,
    "grades": {
        "math": 85,
        "science": 92,
        "history": 78
    },
    "contact": {
        "email": "johndoe@example.com",
        "phone": "1234567890"
    }
}
# Accessing nested dictionary values
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Math Grade:", student["grades"]["math"])
print("Email:", student["contact"]["email"])