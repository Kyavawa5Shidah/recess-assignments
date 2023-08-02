#Inheritance
#Example 1
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing...")

#Create Animal objects
animal = Animal("Generic Animal")
dog = Dog("Spot")
cat = Cat("Fluffy")

#Invoke call eat method
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()

#Example2 Demonstrating inheritance
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

    def move(self):
        print("Moving the vehicle...")

class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print("Number of wheels:", self.num_wheels)

    def honk(self):
        print("Honking the horn...")

#Craete a car object
my_car = Car("Toyota", "Red", 4)

#Access and modify the car attributes
print("Brand:", my_car.brand)
my_car.color = "Blue"

#Invoke the car methods
my_car.display_info()
my_car.move()
my_car.honk()

#Exercise 1
#Demonstrate using inheritance to calculate area and perimeter of a circle and rectangle respectively (SHape : Circle)
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
#creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

#invoke methods for the circle
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()
print("Area of the circle:", circle_area)
print("Perimeter of the circle:", circle_perimeter)

#invoke methods for the rectangle
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
print("Area of the rectangle:", rectangle_area)
print("Perimeter of the rectangle:", rectangle_perimeter)


#Example 3
#Multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        super().display_info()
        print(f"Species:{self.species}")
        print(f"Name: {self.name}")

#Create a bird object
my_bird = Bird("Pigeon", "bird")

#Invoke the bird methods
my_bird.eat()
my_bird.fly()

#Method overriding
class Animal:
    def make_sound(self):
        print("Animal is making a sound!")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking!")

class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing!")

def make_animal_sound(animal):
    animal.make_sound()

#Create  an object
animal = Animal()
dog = Dog()
cat = Cat()

#Calling make_animal_sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

#Polymorohism allows you to write code that can work with different objects
#Method Overriding occurs when a derived class, subclass, (child class), provides its own
#Implementation of a method that is already defined in its base class, super class
#Method overloading allows a class to have multiple methods with the same name but different parameters

#Example4
class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2
    
    def calculate_circumference(self):
        return 2* 3.14 * self.radius
    
#Calculate shape objects
rectangle = Rectangle(5, 5)
circle = Circle(5)
    
#Calculate Display area
print("Area of rectangle:", rectangle.calculate_area())
print("Area of circle:", circle.calculate_circumference())

#Abstraction
#Allow you to focus on essential features and hide them from unnecessary details

#Example 5: Demonstrate abstractions
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting the car...")

    def stop(self):
        print("Stopping the car...")

class Truck(Vehicle):
    def start(self):
        print("Starting the truck...")

    def stop(self):
        print("Stopping the truck...")

#Create vehicle objects
car = Car()
truck = Truck()

#start the vehicle
car.start()
truck.start()

#stop the truck
truck.stop()
car.stop()

#Exercise 2: Demonstrate abstraction using calculating area of a circle and rectangle

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
#Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

#invoke the methods
print("Area of the circle:", circle.calculate_area())
print("Area of the rectangle:", rectangle.calculate_area()) 


#Assignment 1: Create a receipt printing program with GUI interface a more advanced detail earns you more points

import tkinter as tk

class ReceiptApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Receipt Printing Program")
        
        self.items = []
        self.quantities = []
        self.prices = []

        # Item Name entry
        self.item_label = tk.Label(master, text="Item Name:")
        self.item_label.pack()
        self.item_entry = tk.Entry(master)
        self.item_entry.pack()
        
        # Quantity entry
        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        # Price entry
        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        # Add button
        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.pack()
        
        # Receipt text widget
        self.receipt_text = tk.Text(master, height=10, width=30)
        self.receipt_text.pack()
        
        # Print receipt button
        self.print_button = tk.Button(master, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()
    
    def add_item(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if item and quantity:
            self.items.append(item)
            self.quantities.append(quantity)
            self.prices.append(price)

            self.receipt_text.insert(tk.END, f"Item: {item} (Quantity: {quantity}, Price: {price})\n")
        
        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
    
    def print_receipt(self):
     total_amount = sum(float(price) * int(quantity) for price, quantity in zip(self.prices, self.quantities))

        # Display the total amount in the receipt
     self.receipt_text.insert(tk.END, f"\nTotal Amount: {total_amount:.2f}\n")

if __name__ == "__main__":
 root = tk.Tk()
 app = ReceiptApp(root)
 root.mainloop()