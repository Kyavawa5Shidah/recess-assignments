#store multiple items in a single variable
#unchangeable but one can can remove and add new items

setone = {"benz", "tx", "vitz"}
print(setone)

#Duplicate in sets
setone = {"benz", "tx", "vitz", "vitz"}
print(setone)

#length of the set
setone = {"benz", "tx", "vitz"}
print("Set length is:")
print(len(setone))

#datatype of set
setone = {"benz", "tx", "vitz"}
print("Set datatype is")
print(type(setone))

#Accessing items in set
setone = {"benz", "tx", "vitz"}
for item in setone:
    print(item)

#Adding item
setone = {"benz", "tx", "vitz"}
setone.add("bmw")
print(setone)

#Add two sets together
setone = {"benz", "tx", "vitz"}
settwo = {1, 2, 3}
setthree = setone.union(settwo)
print(setthree)