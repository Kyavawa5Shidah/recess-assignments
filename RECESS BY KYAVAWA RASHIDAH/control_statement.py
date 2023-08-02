#if condition1:
#print('True') # code lock is only exeecuted if condition1 is True
#elif condition2:
#print('True') # code block is only executed if condition2 is True
#else:
#print('False)


#Example 1
#<18, Print "You are under age"
# age >= 18 and age <= 65 "You are an adult"
# print "Your are a senior citizen"

age = 25
if age < 18:
    print('You are under age')
elif age >= 18 and age <= 65:
    print('You are an adult')
else:
    print('You are a senior citizen')

#Loops
#Loops (for, while)

cars = ["Telsa", "Jeep", "Ford", "Toyota", "BMW"]
for car in cars:
    print(car)

#Example 2
#fruits 
fruits = ["apple", "banana", "mango", "pineapple"]
for fruit in fruits:
    print(fruit)

# while loop
# while condition is true: It will execute while condition is True:

x = 0
while x < 5:
    print(x)
    x += 1

#Example 3
phones = ["oppo", "iphone", "tecno", "samsung"]
# Convert the set of phones to a list
phone_list = list(phones)
# Get the length of the phone list
length = len(phone_list)
# Initialize the index variable
index = 0
while index < length:
    # Access the current phone
    current_phone = phone_list[index]
    print(current_phone)
    index += 1

#Break and continue statements
#Break statement

for number in range(1,10):
    if number == 5:
        break
    print(number)

#Continue statement
for number in range(1,10):
    if number == 5:
        continue
    print(number)

#Example 4
phones = ["oppo", "iphone", "tecno", "samsung"]
for phone in phones:
    if phone == "iphone":
      continue
    if phone == "tecno":
      break
print(phone)

 #Exception handling (try, except, finally)
try:
    x = 10/0
except ZeroDivisionError:
    print('Error: Division by Zero')# cannot divide by zero
finally:
    print('This is always executed') #complete execution

#Example 5
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid types for division.")
    finally:
        print("Division operation completed.")


# Test cases
divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero error
divide_numbers(10, "2")  # Type error


#Dict is a dictionary {}

emotion = {
    'happy': "I'm glad to hear you are happy",
    'sad': "I'm sorry to hear that  you are sad",
    'Angry': "take a deep breath and try to stay alive",
    'fearful': "I understand that fear can be challenging",
    'disgusted': "that's unfortunate to feel disgusted",

}
#Prompt the user to enter their emotions
user_emotion = input("How are u feeling today?")

#convert the user input to enter their emotions
user_emotion = user_emotion.lower()


if user_emotion in emotion:
    print(emotion[user_emotion])

else:
        print("I'm sorry i don't understand your emotion.")

#exercise 1
#write a program to ask students about their mental health
# Prompt students on a scale of 1 to 10 to rate their mental health

def get_mental_health_ratings(students):
    ratings = {}

    for student in students:
        print("Student:", student)
        rating = input("Please rate your mental health on a scale of 1 to 10: ")

        # Validate the input
        while not rating.isdigit() or int(rating) < 1 or int(rating) > 10:
            print("Invalid rating. Please enter a number between 1 and 10.")
            rating = input("Please rate your mental health on a scale of 1 to 10: ")

        # Store the rating in the dictionary
        ratings[student] = int(rating)
    return ratings

# Test case
student_list = ["Alice", "Bob", "Charlie"]
ratings_dict = get_mental_health_ratings(student_list)

# Print the ratings
print("\nMental Health Ratings:")
for student, rating in ratings_dict.items():
    print(student + ": " + str(rating))