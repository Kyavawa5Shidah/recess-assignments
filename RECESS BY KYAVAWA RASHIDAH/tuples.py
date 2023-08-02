#Floats, strings, int, decimal, char, booleans
print("********TYPE OF******")
w =40 #int type
print(type(w))
z = "Hello world"#string type
print(type(z))
y = 1j #complex type
print(type(y))
print("************")

#LISTS
#They are used to store multiple items in a single variable
#Lists are ordered, changeable and allows duplicate values
print("LISTS")
Afternoon = ["Shidah", "Cassie", "Maria", "Jose"]
print(Afternoon)
#List length
print(len(Afternoon))
#List type
print(type(Afternoon))

#print List items using index
print("************")
print(Afternoon[0])
print(Afternoon[2])
print(Afternoon[3])
print(Afternoon[-2])

#Accessing a range of items, get"s from the start index to monus one of the last index
print("************")
print(Afternoon[3:6])
print(Afternoon[:3])
print(Afternoon[1:])

#print List items using a loop
print("***************")
for i in Afternoon:
    print(i)

#appending
Afternoon.append("Me")
print(Afternoon)

 #Remove a particular item
Afternoon.remove("Maria")
print(Afternoon)

 #Add list items using the insert method
Afternoon.insert(0, "Pearl")
print(Afternoon)

 #Remove a particular item using index
Afternoon.pop(0)
print(Afternoon)

 #TUPLES
 #They are used to store items in a single variable
 #They are ordered and unchangeable
print("TUPLES")
phones = ("samsung", "hawueii", "tecno", "iphone")
print(phones)

 #Duplication in tuples
phones = ("samsung", "hawueii", "tecno", "iphone", "iphone")

 #use the len() with this tuple example
print(" The tuple length is")
print(len(phones))

 #Tuples showing different data types
Tupleone = ("short", "dress", "shirt")
Tupletwo = ( 10000, 2000 ,4000, 5000)

 #How to access tuples
print(Tupleone[-1])
print(Tupletwo[1])

 #Add items to a tuple
phones = ("samsung", "hawueii", "tecno", "iphone")
phones_added = phones + ("oppo", "camon")
print(phones_added)