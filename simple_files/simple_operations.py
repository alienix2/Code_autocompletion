# Addition of two numbers
x = 10
y = 20
z = x + y
print("The sum is:", z)

# Another example of addition
a = 5
b = 15
c = a + b
print("The total is:", c)

# Age check
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Another age check example
user_age = 17
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Loop through range
for i in range(5):
    print("Number:", i)

# Another loop example
for num in range(3):
    print("Current number:", num)

# Countdown using while loop
count = 5
while count > 0:
    print("Count:", count)
    count -= 1

# Another countdown example
timer = 3
while timer > 0:
    print("Time left:", timer)
    timer -= 1

# Function to calculate square
def square(n):
    return n * n
result = square(4)
print("Square of 4 is:", result)

# Another function example
def cube(n):
    return n * n * n
output = cube(3)
print("Cube of 3 is:", output)

# Sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print("Sum of numbers:", sum_numbers)

# Another sum example
values = [5, 10, 15, 20, 25]
total_sum = 0
for value in values:
    total_sum += value
print("Total sum of values:", total_sum)

# Access and print dictionary values
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"], "is", person["age"], "years old.")

# Another dictionary example
employee = {"name": "John", "age": 28, "department": "Engineering"}
print(employee["name"], "works in", employee["department"])

# Concatenate strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Another string concatenation example
first = "Sarah"
last = "Johnson"
full = first + " " + last
print("Full name:", full)

# User input
name = input("Enter your name: ")
print("Hello,", name)

# Another user input example
username = input("Enter your username: ")
print("Welcome,", username)

# Basic arithmetic operations
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Another arithmetic example
x = 12
y = 4
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)
print("Remainder:", x % y)

# Even or odd check
num = 7
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

# Another even or odd check example
number = 14
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Function to find the maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print("Max of 10 and 20 is:", max_of_two(10, 20))

# Another max function example
def min_of_two(a, b):
    if a < b:
        return a
    else:
        return b
print("Min of 10 and 20 is:", min_of_two(10, 20))

# Reverse a string
text = "hello"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

# Another reverse string example
word = "programming"
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))

# Another palindrome check example
print("Is 'noon' a palindrome?", is_palindrome("noon"))

# List comprehension to get even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Another list comprehension example
odd_numbers = [x for x in range(10) if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Define a class with a method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person = Person("Alice", 30)
person.greet()

# Another class example
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"This car is a {self.make} {self.model}.")
car = Car("Toyota", "Corolla")
car.display()

# Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Another file write example
with open("sample.txt", "w") as file:
    file.write("Sample text")

# Read from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Another file read example
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Try-except block for error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Another try-except block example
try:
    result = int("abc")
except ValueError:
    print("Invalid number!")

# Tuple indexing
my_tuple = (1, 2, 3, 4)
print(my_tuple[1])

# Another tuple example
my_tuple = (10, 20, 30, 40)
print(my_tuple[2])

# Set operations
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

# Another set example
my_set = {10, 20, 30, 40, 50}
my_set.add(60)
print(my_set)

# Map function to square numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# Another map function example
numbers = [10, 20, 30, 40, 50]
cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers)

# Filter function to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Another filter function example
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Sum of numbers using loop
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print(sum_numbers)

# Another sum using loop example
total = 0
for num in numbers:
    total += num
print(total)

# Lambda function for multiplication
multiply = lambda x, y: x * y
print(multiply(5, 3))

# Another lambda function example
multiply = lambda x, y: x * y
print(multiply(7, 8))

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Another nested loop example
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))

# Another recursive function example
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
print("2 to the power of 3 is:", power(2, 3))

# List slicing
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])

# Another list slicing example
my_list = [10, 20, 30, 40, 50]
print(my_list[2:4])

# Dictionary comprehension to square numbers
squared_numbers = {x: x * x for x in range(5)}
print(squared_numbers)

# Another dictionary comprehension example
cubed_numbers = {x: x**3 for x in range(10)}
print("Cubed numbers:", cubed_numbers)

# Define a class with a method
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"The {self.species} named {self.name} makes a sound.")
dog = Animal("Rex", "dog")
dog.make_sound()

# Another class example
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"The {self.color} cat named {self.name} meows.")
cat = Cat("Whiskers", "black")
cat.meow()

# List operations
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

# Another list operation example
fruits = ["mango", "pineapple", "grape"]
fruits.append("kiwi")
print(fruits)
fruits.remove("pineapple")
print(fruits)

# String formatting
greeting = "Hello, {}. Welcome to {}."
print(greeting.format("Alice", "Wonderland"))

# Another string formatting example
message = "Hi, {}. Welcome to {}."
print(message.format("John", "Programming"))

# Access nested dictionary values
students = {"Alice": {"age": 25, "grade": "A"}, "Bob": {"age": 22, "grade": "B"}}
print(students["Alice"]["grade"])

# Another nested dictionary example
employees = {
    "Alice": {"age": 28, "position": "Manager"},
    "Bob": {"age": 24, "position": "Developer"},
}
print(employees["Bob"]["position"])

# Swap variables
a, b = b, a
print("a:", a, "b:", b)

# Another swap variables example
x, y = y, x
print("x:", x, "y:", y)

# List slicing examples
my_list = list(range(10))
print(my_list[2:5])
print(my_list[:4])
print(my_list[6:])
print(my_list[::2])
print(my_list[::-1])

# Another list slicing example
my_list = list(range(20))
print(my_list[5:10])
print(my_list[:5])
print(my_list[15:])
print(my_list[::2])
print(my_list[::-2])

# List comprehension to get squared even numbers
squared_even_numbers = [x * x for x in range(10) if x % 2 == 0]
print(squared_even_numbers)

# Another list comprehension example
squared_odd_numbers = [x ** 2 for x in range(20) if x % 2 != 0]
print("Squared odd numbers:", squared_odd_numbers)

# Create a matrix using list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

# Another matrix example
matrix = [[i * j for j in range(5)] for i in range(5)]
print(matrix)

# Dictionary comprehension to get squared numbers
squared_numbers_dict = {x: x * x for x in range(10) if x % 2 == 0}
print(squared_numbers_dict)

# Another dictionary comprehension example
cubed_odd_numbers = {x: x ** 3 for x in range(20) if x % 2 != 0}
print("Cubed odd numbers:", cubed_odd_numbers)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Another merging dictionaries example
dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

# Find max value in a list
max_value = max([1, 2, 3, 4, 5])
print("Max value:", max_value)

# Another max value example
max_val = max([10, 20, 30, 40, 50])
print("Max value:", max_val)

# Find min value in a list
min_value = min([1, 2, 3, 4, 5])
print("Min value:", min_value)

# Another min value example
min_val = min([10, 20, 30, 40, 50])
print("Min value:", min_val)

# Calculate the sum of a list
total = sum([1, 2, 3, 4, 5])
print("Total sum:", total)

# Another sum calculation example
total_sum = sum([10, 20, 30, 40, 50])
print("Total sum:", total_sum)

# Reverse a list
reversed_list = [1, 2, 3, 4, 5][::-1]
print("Reversed list:", reversed_list)

# Another reverse list example
reversed_list = [10, 20, 30, 40, 50][::-1]
print("Reversed list:", reversed_list)

# List comprehension to get squares of numbers
squares = [x * x for x in range(10)]
print("Squares:", squares)

# Another list comprehension example
cubes = [x ** 3 for x in range(10)]
print("Cubes:", cubes)

# Check if an element is in a list
print(3 in [1, 2, 3, 4, 5])

# Another element check example
print(20 in [10, 20, 30, 40, 50])

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# Another list concatenation example
list1 = [5, 10, 15]
list2 = [20, 25, 30]
combined = list1 + list2
print("Combined list:", combined)

# Repeat elements in a list
repeated_list = [1, 2, 3] * 3
print("Repeated list:", repeated_list)

# Another repeat elements example
repeated = [15, 25, 35] * 2
print("Repeated list:", repeated)

# Get the length of a list
print("Length of list:", len([1, 2, 3, 4, 5]))

# Another length of list example
print("Length of list:", len([15, 25, 35, 45, 55]))

# Access first and last elements of a list
print("First element:", [1, 2, 3, 4, 5][0])
print("Last element:", [1, 2, 3, 4, 5][-1])

# Another access elements example
print("First element:", [5, 10, 15, 20, 25][0])
print("Last element:", [5, 10, 15, 20, 25][-1])

# Modify an element in a list
my_list = [1, 2, 3, 4, 5]
my_list[0] = 10
print("Modified list:", my_list)

# Another modify element example
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print("Modified list:", my_list)

# Delete an element from a list
del my_list[0]
print("List after deletion:", my_list)

# Another delete element example
del my_list[1]
print("List after deletion:", my_list)

# Insert an element in a list
my_list.insert(0, 1)
print("List after insertion:", my_list)

# Another insert element example
my_list.insert(1, 10)
print("List after insertion:", my_list)

# Pop an element from a list
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Another pop element example
popped = my_list.pop()
print("Popped element:", popped)
print("List after popping:", my_list)

# Clear a list
my_list.clear()
print("List after clearing:", my_list)

# Another clear list example
my_list.clear()
print("List after clearing:", my_list)

# Addition of two numbers
a = 12
b = 25
c = a + b
print("The sum is:", c)

# Another example of addition
num1 = 7
num2 = 18
total = num1 + num2
print("The total is:", total)

# Age check
age = 21
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Another age check example
voter_age = 15
if voter_age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# Loop through range
for i in range(6):
    print("Number:", i)

# Another loop example
for index in range(4):
    print("Current index:", index)

# Countdown using while loop
counter = 4
while counter > 0:
    print("Counter:", counter)
    counter -= 1

# Another countdown example
timer = 6
while timer > 0:
    print("Time remaining:", timer)
    timer -= 1

# Function to calculate square
def square(n):
    return n * n
result = square(5)
print("Square of 5 is:", result)

# Another function example
def cube(n):
    return n * n * n
output = cube(4)
print("Cube of 4 is:", output)

# Sum of numbers in a list
values = [2, 4, 6, 8, 10]
sum_values = 0
for value in values:
    sum_values += value
print("Sum of values:", sum_values)

# Another sum example
numbers = [3, 6, 9, 12]
total_sum = 0
for num in numbers:
    total_sum += num
print("Total sum of numbers:", total_sum)

# Access and print dictionary values
person = {"name": "Bob", "age": 30, "city": "Seattle"}
print(person["name"], "is", person["age"], "years old.")

# Another dictionary example
employee = {"name": "David", "age": 35, "department": "HR"}
print(employee["name"], "works in", employee["department"])

# Concatenate strings
first_name = "Emma"
last_name = "Watson"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Another string concatenation example
first = "Olivia"
last = "Brown"
complete_name = first + " " + last
print("Complete name:", complete_name)

# User input
username = input("Enter your username: ")
print("Welcome,", username)

# Another user input example
user_input = input("Enter your favorite color: ")
print("Your favorite color is", user_input)

# Basic arithmetic operations
x = 14
y = 5
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)

# Another arithmetic example
m = 18
n = 6
print("Sum:", m + n)
print("Difference:", m - n)
print("Product:", m * n)
print("Quotient:", m / n)
print("Remainder:", m % n)

# Even or odd check
number = 8
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Another even or odd check example
value = 11
if value % 2 == 0:
    print(value, "is even.")
else:
    print(value, "is odd.")

# Function to find the maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print("Max of 15 and 25 is:", max_of_two(15, 25))

# Another max function example
def min_of_two(x, y):
    if x < y:
        return x
    else:
        return y
print("Min of 10 and 20 is:", min_of_two(10, 20))

# Reverse a string
text = "world"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

# Another reverse string example
word = "Python"
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
print("Is 'madam' a palindrome?", is_palindrome("madam"))

# Another palindrome check example
print("Is 'level' a palindrome?", is_palindrome("level"))

# List comprehension to get even numbers
even_numbers = [x for x in range(12) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Another list comprehension example
odd_numbers = [x for x in range(12) if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Define a class with a method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Charlie", 29)
person1.greet()

# Another class example
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"This car is a {self.make} {self.model}.")
car1 = Car("Honda", "Civic")
car1.display()

# Write to a file
with open("test.txt", "w") as file:
    file.write("Testing file write.")

# Another file write example
with open("output.txt", "w") as file:
    file.write("Output file example.")

# Read from a file
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# Another file read example
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# Try-except block for error handling
try:
    result = 20 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Another try-except block example
try:
    result = int("xyz")
except ValueError:
    print("Invalid integer!")

# Tuple indexing
my_tuple = (2, 4, 6, 8)
print(my_tuple[2])

# Another tuple example
tuple_data = (12, 24, 36, 48)
print(tuple_data[3])

# Set operations
num_set = {2, 4, 6, 8}
num_set.add(10)
print(num_set)

# Another set example
value_set = {15, 30, 45, 60}
value_set.add(75)
print(value_set)

# Map function to square numbers
numbers = [2, 4, 6, 8, 10]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# Another map function example
values = [5, 10, 15, 20]
cubed_values = list(map(lambda x: x**3, values))
print(cubed_values)

# Filter function to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, values))
print(even_numbers)

# Another filter function example
odd_values = list(filter(lambda x: x % 2 != 0, values))
print(odd_values)

# Sum of numbers using loop
sum_numbers = 0
for num in values:
    sum_numbers += num
print(sum_numbers)

# Another sum using loop example
total = 0
for value in numbers:
    total += value
print(total)

# Lambda function for multiplication
multiply = lambda x, y: x * y
print(multiply(6, 4))

# Another lambda function example
product = lambda a, b: a * b
print(product(9, 7))

# Nested loops
for i in range(4):
    for j in range(4):
        print(f"i={i}, j={j}")

# Another nested loop example
for x in range(3):
    for y in range(3):
        print(f"x={x}, y={y}")

# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 6 is:", factorial(6))

# Another recursive function example
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
print("3 to the power of 4 is:", power(3, 4))

# List slicing
my_list = [2, 4, 6, 8, 10]
print(my_list[1:4])

# Another list slicing example
values = [10, 20, 30, 40, 50]
print(values[2:4])

# Dictionary comprehension to square numbers
squared_numbers = {x: x * x for x in range(6)}
print(squared_numbers)

# Another dictionary comprehension example
cubed_numbers = {x: x**3 for x in range(8)}
print("Cubed numbers:", cubed_numbers)

# Define a class with a method
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"The {self.species} named {self.name} makes a sound.")
dog = Animal("Max", "dog")
dog.make_sound()

# Another class example
class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def chirp(self):
        print(f"The {self.color} bird named {self.name} chirps.")
parrot = Bird("Polly", "green")
parrot.chirp()

# List operations
fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
print(fruits)
fruits.remove("banana")
print(fruits)

# Another list operation example
vegetables = ["carrot", "broccoli", "spinach"]
vegetables.append("peas")
print(vegetables)
vegetables.remove("broccoli")
print(vegetables)

# String formatting
greeting = "Hello, {}. Welcome to {}."
print(greeting.format("John", "Python"))

# Another string formatting example
message = "Hey, {}. Good to see you at {}."
print(message.format("Jane", "the event"))

# Access nested dictionary values
students = {"Alice": {"age": 22, "grade": "B"}, "Bob": {"age": 24, "grade": "A"}}
print(students["Bob"]["grade"])

# Another nested dictionary example
employees = {
    "David": {"age": 35, "position": "Manager"},
    "Carol": {"age": 28, "position": "Developer"},
}
print(employees["Carol"]["position"])

# Swap variables
a, b = b, a
print("a:", a, "b:", b)

# Another swap variables example
x, y = y, x
print("x:", x, "y:", y)

# List slicing examples
my_list = list(range(12))
print(my_list[2:5])
print(my_list[:4])
print(my_list[6:])
print(my_list[::2])
print(my_list[::-1])

# Another list slicing example
values = list(range(20))
print(values[5:10])
print(values[:5])
print(values[15:])
print(values[::2])
print(values[::-2])

# List comprehension to get squared even numbers
squared_even_numbers = [x * x for x in range(12) if x % 2 == 0]
print(squared_even_numbers)

# Another list comprehension example
squared_odd_numbers = [x ** 2 for x in range(15) if x % 2 != 0]
print("Squared odd numbers:", squared_odd_numbers)

# Create a matrix using list comprehension
matrix = [[j for j in range(4)] for i in range(4)]
print(matrix)

# Another matrix example
matrix = [[i * j for j in range(4)] for i in range(4)]
print(matrix)

# Dictionary comprehension to get squared numbers
squared_numbers_dict = {x: x * x for x in range(12) if x % 2 == 0}
print(squared_numbers_dict)

# Another dictionary comprehension example
cubed_odd_numbers = {x: x ** 3 for x in range(15) if x % 2 != 0}
print("Cubed odd numbers:", cubed_odd_numbers)

# Merging dictionaries
dict1 = {"a": 2, "b": 3}
dict2 = {"b": 4, "c": 5}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Another merging dictionaries example
dict1 = {"x": 5, "y": 6}
dict2 = {"y": 7, "z": 8}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

# Find max value in a list
max_value = max([2, 4, 6, 8, 10])
print("Max value:", max_value)

# Another max value example
max_val = max([15, 25, 35, 45])
print("Max value:", max_val)

# Find min value in a list
min_value = min([2, 4, 6, 8, 10])
print("Min value:", min_value)

# Another min value example
min_val = min([15, 25, 35, 45])
print("Min value:", min_val)

# Calculate the sum of a list
total = sum([2, 4, 6, 8, 10])
print("Total sum:", total)

# Another sum calculation example
total_sum = sum([15, 25, 35, 45])
print("Total sum:", total_sum)

# Reverse a list
reversed_list = [2, 4, 6, 8, 10][::-1]
print("Reversed list:", reversed_list)

# Another reverse list example
reverse_values = [15, 25, 35, 45][::-1]
print("Reversed list:", reverse_values)

# List comprehension to get squares of numbers
squares = [x * x for x in range(12)]
print("Squares:", squares)

# Another list comprehension example
cubes = [x ** 3 for x in range(8)]
print("Cubes:", cubes)

# Check if an element is in a list
print(4 in [2, 4, 6, 8, 10])

# Another element check example
print(25 in [15, 25, 35, 45])

# Concatenate two lists
list1 = [2, 4, 6]
list2 = [8, 10, 12]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# Another list concatenation example
list1 = [5, 10, 15]
list2 = [20, 25, 30]
combined = list1 + list2
print("Combined list:", combined)

# Repeat elements in a list
repeated_list = [3, 6, 9] * 3
print("Repeated list:", repeated_list)

# Another repeat elements example
repeated = [10, 20, 30] * 2
print("Repeated list:", repeated)

# Get the length of a list
print("Length of list:", len([3, 6, 9, 12, 15]))

# Another length of list example
print("Length of list:", len([10, 20, 30, 40, 50]))

# Access first and last elements of a list
print("First element:", [3, 6, 9, 12, 15][0])
print("Last element:", [3, 6, 9, 12, 15][-1])

# Another access elements example
print("First element:", [10, 20, 30, 40, 50][0])
print("Last element:", [10, 20, 30, 40, 50][-1])

# Modify an element in a list
my_list = [3, 6, 9, 12, 15]
my_list[0] = 5
print("Modified list:", my_list)

# Another modify element example
values = [10, 20, 30, 40, 50]
values[1] = 25
print("Modified list:", values)

# Delete an element from a list
del my_list[0]
print("List after deletion:", my_list)

# Another delete element example
del values[1]
print("List after deletion:", values)

# Insert an element in a list
my_list.insert(0, 3)
print("List after insertion:", my_list)

# Another insert element example
values.insert(1, 20)
print("List after insertion:", values)

# Pop an element from a list
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Another pop element example
popped_value = values.pop()
print("Popped element:", popped_value)
print("List after popping:", values)

# Clear a list
my_list.clear()
print("List after clearing:", my_list)

# Another clear list example
values.clear()
print("List after clearing:", values)
