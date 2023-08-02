
#Regular expressions
"""
_summary_
\d: Matches any digit (0-9)
"""

#Matching and searching
#regex re.match(), re.search(), re.findall()

#Example 1
#Demonstrating regex | Match first word, match group word, match all numbers
import re
text = "Hello, my name is Shidah. I am a programmer with 10 years of experience."

#Match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Match:", match.group())

matches = re.findall(r"\d+", text)
print("Matches:", matches)

#Example 2 : Validate email format or email address
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    
    else:
        return False

#Example usage
email1 = "kyavawarashidah5@gmail.com"
email2 ="egdjbjjlk56gmail.com"

print(validate_email(email1))
print(validate_email(email2))

#Generators and iterators
#'yeild generator
#Iterator'__iter__' "__next__" iterator

def factorial(n):
    #Return the factorial of a number
    if n == 0:
        yield 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        yield fact

     
#print the factorial of a number from 1 - 10
for i in range(1 , 10):
     print(*factorial(i))

#Example 3
#Generate function that yields the square of numbers from 1 to 10

def squares():
    for i in range(1, 10):
        yield i ** 2

#create an iterator object that yields te square numbers from 1 to 10
squares_iterator = squares()

#Print the first five square numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))


#decorator @my decorator

def my_decorator(func):
    def inner():
      print("This is the decorator")
      func()
    return inner 

@my_decorator
def outer_decorator():
    print("This is the outer decorator")

outer_decorator()

#Context Manager - is an object that defines a temporary context for a block of code

#Example1: Demonstrate a context manager to open a file and returns a context manager instance
"""
def open_file(filename):
    #Open a file and return a context manager instance
    file = open(filename, "r")

    def __enter__():
        return file
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        file.close()

        return __enter__.__exit__
    
with open_file("my_file.txt") as f:
    contents = f.read()
"""
#Example 2: Demonstrate a context manager using a time series
import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f'the time for this execution{execution_time} seconds elapsed')

#With example usage
with Timer():
    #measure the execution time
    time.sleep(2)

#multithreading and multiprocessing
#techniques that can be used to improve performance of a Python program

#Multithreading is a technique where multiple threads are created within a single process.
#Muliprocessing is a technique where multiple threads are created

#Example of multithreading
import threading

def task(name):
    print(f"Running task{name}")

#create multiple threads
threads = []
for i in range(10):
    t = threading.Thread(target=task, args = {f"Thread {i}",})
    threads.append(t)
    t.start()

#wait for all threads to finish

for t in threads:
    t.join()

# Example 4: Demonstrate use of multiprocessing
#import multiprocessing

#def process_task(name):
    #print(f"Processing task {name}")

#create a pool of processes
#pool = multiprocessing.Pool(processes=5)

#submit multiple task to the pool
#for i in range(6):
    #pool.apply_async(process_task, args=(f"Process {i}",))

#close the pool and wait for all process to finish
#pool.close()
#pool.join()

#example5: demonstrate use of multithreading and multiprocessing
import threading
import multiprocessing

def task(name):
    print(f"running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

#create multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

#wait for all threads to finish
for t in threads:
    t.join()

#Assignment
#1. Show a context manager for file handling that automatically opens and closes a file
from contextlib import contextmanager

@contextmanager
def open_file(file_path, mode):
    try:
        file = open(file_path, mode)
        yield file
    finally:
        file.close()

# Example usage:
file_path = "path/to/your/file.txt"
mode = "r"  # Use "w" for writing, "a" for appending, etc.

with open_file(file_path, mode) as file:
    #Perform file operations here
     content = file.read()
     print(content)

#2. show a context manager for managing a database connection
import psycopg2
from contextlib import contextmanager

@contextmanager
def db_connection(db_params):
    conn = psycopg2.connect(**db_params)
    try:
        yield conn
    finally:
        conn.close()

# Example usage:
db_params = {
    "host": "localhost",
    "port": 5432,
    "database": "your_database",
    "user": "your_username",
    "password": "your_password"
}

with db_connection(db_params) as conn:
    # Perform database operations here
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
#3. Show a multithreading and multiprocessing that allows us to run the function for different amounts of time
import time
from threading import Thread
from multiprocessing import Process

def my_function(duration):
    print(f"Running my_function for {duration} seconds...")
    time.sleep(duration)
    print("Finished running my_function.")

# Multithreading example
def run_with_threads():
    durations = [2, 4, 6]  # Different durations for each thread

    threads = []
    for duration in durations:
        thread = Thread(target=my_function, args=(duration,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Multiprocessing example
def run_with_processes():
    durations = [2, 4, 6]  # Different durations for each process

    processes = []
    for duration in durations:
        process = Process(target=my_function, args=(duration,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

# Run examples
print("Running with threads:")
run_with_threads()

print("\nRunning with processes:")
run_with_processes()