#works when one wants to combine a string to a number
#we need to use the format() method
# the format () takes the passed parameters, format then places
#then in the string where the placeholders {} are

age = 23
#name = "My name is Rashidah, I am " + age
name = "My name is Rashidah and I am {}"

print(name.format(age))