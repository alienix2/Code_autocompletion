x = 10
y = 20
z = x + y
print("The sum is:", z)

age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

for i in range(5):
    print("Number:", i)

count = 5
while count > 0:
    print("Count:", count)
    count -= 1

def square(n):
    return n * n
result = square(4)
print("Square of 4 is:", result)

numbers = [1, 2, 3, 4, 5]
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print("Sum of numbers:", sum_numbers)

person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"], "is", person["age"], "years old.")

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

name = input("Enter your name: ")
print("Hello,", name)

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

num = 7
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")


def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


print("Max of 10 and 20 is:", max_of_two(10, 20))

text = "hello"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)


def is_palindrome(s):
    return s == s[::-1]


print("Is 'racecar' a palindrome?", is_palindrome("racecar"))

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person = Person("Alice", 30)
person.greet()

with open("example.txt", "w") as file:
    file.write("Hello, world!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

my_tuple = (1, 2, 3, 4)
print(my_tuple[1])

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

sum_numbers = 0
for num in numbers:
    sum_numbers += num
print(sum_numbers)

multiply = lambda x, y: x * y
print(multiply(5, 3))

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5 is:", factorial(5))

my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])

squared_numbers = {x: x * x for x in range(5)}
print(squared_numbers)


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print(f"The {self.species} named {self.name} makes a sound.")
dog = Animal("Rex", "dog")
dog.make_sound()

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

greeting = "Hello, {}. Welcome to {}."
print(greeting.format("Alice", "Wonderland"))

students = {"Alice": {"age": 25, "grade": "A"}, "Bob": {"age": 22, "grade": "B"}}
print(students["Alice"]["grade"])

a, b = b, a
print("a:", a, "b:", b)

my_list = list(range(10))
print(my_list[2:5])
print(my_list[:4])
print(my_list[6:])
print(my_list[::2])
print(my_list[::-1])

squared_even_numbers = [x * x for x in range(10) if x % 2 == 0]
print(squared_even_numbers)

matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

squared_numbers_dict = {x: x * x for x in range(10) if x % 2 == 0}
print(squared_numbers_dict)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

max_value = max([1, 2, 3, 4, 5])
print("Max value:", max_value)

min_value = min([1, 2, 3, 4, 5])
print("Min value:", min_value)

total = sum([1, 2, 3, 4, 5])
print("Total sum:", total)

reversed_list = [1, 2, 3, 4, 5][::-1]
print("Reversed list:", reversed_list)

squares = [x * x for x in range(10)]
print("Squares:", squares)

print(3 in [1, 2, 3, 4, 5])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

repeated_list = [1, 2, 3] * 3
print("Repeated list:", repeated_list)

print("Length of list:", len([1, 2, 3, 4, 5]))

print("First element:", [1, 2, 3, 4, 5][0])
print("Last element:", [1, 2, 3, 4, 5][-1])

my_list = [1, 2, 3, 4, 5]
my_list[0] = 10
print("Modified list:", my_list)

del my_list[0]
print("List after deletion:", my_list)

my_list.insert(0, 1)
print("List after insertion:", my_list)

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

my_list.clear()
print("List after clearing:", my_list)

x = 30
y = 40
z = x + y
print("The sum is:", z)

age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

for i in range(10):
    print("Number:", i)

count = 3
while count > 0:
    print("Count:", count)
    count -= 1


def cube(n):
    return n * n * n
result = cube(3)
print("Cube of 3 is:", result)

numbers = [6, 7, 8, 9, 10]
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print("Sum of numbers:", sum_numbers)

person = {"name": "Bob", "age": 30, "city": "San Francisco"}
print(person["name"], "is", person["age"], "years old.")

first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name
print("Full name:", full_name)

name = input("Enter your name: ")
print("Hello,", name)

a = 15
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

num = 9
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")


def min_of_two(a, b):
    if a < b:
        return a
    else:
        return b
print("Min of 10 and 20 is:", min_of_two(10, 20))

text = "world"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

def is_palindrome(s):
    return s == s[::-1]
print("Is 'level' a palindrome?", is_palindrome("level"))

odd_numbers = [x for x in range(10) if x % 2 != 0]
print("Odd numbers:", odd_numbers)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"This car is a {self.make} {self.model}.")
car = Car("Toyota", "Corolla")
car.display()

with open("sample.txt", "w") as file:
    file.write("Sample text")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

try:
    result = int("abc")
except ValueError:
    print("Invalid number!")

my_tuple = (5, 10, 15, 20)
print(my_tuple[2])

my_set = {10, 20, 30, 40, 50}
my_set.add(60)
print(my_set)

numbers = [10, 20, 30, 40, 50]
cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers)

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

sum_numbers = 0
for num in numbers:
    sum_numbers += num
print(sum_numbers)

multiply = lambda x, y: x * y
print(multiply(6, 4))

for i in range(4):
    for j in range(4):
        print(f"i={i}, j={j}")


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
print("2 to the power of 3 is:", power(2, 3))

my_list = [2, 4, 6, 8, 10]
print(my_list[1:3])

squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Student {self.name} has grade {self.grade}.")
student = Student("Alice", "A")
student.display()

fruits = ["mango", "pineapple", "grape"]
fruits.append("kiwi")
print(fruits)
fruits.remove("pineapple")
print(fruits)

message = "Hello, {}. Welcome to {}."
print(message.format("Bob", "Python"))

employees = {
    "Alice": {"age": 28, "position": "Manager"},
    "Bob": {"age": 24, "position": "Developer"},
}
print(employees["Bob"]["position"])

a, b = b, a
print("a:", a, "b:", b)

my_list = list(range(20))
print(my_list[5:10])
print(my_list[:5])
print(my_list[15:])
print(my_list[::3])
print(my_list[::-2])

cubed_numbers = [x**3 for x in range(15) if x % 3 == 0]
print(cubed_numbers)

matrix = [[i * j for j in range(5)] for i in range(5)]
print(matrix)

cubed_numbers_dict = {x: x**3 for x in range(10) if x % 3 == 0}
print(cubed_numbers_dict)

dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}
merged_dict = {**dict1, **dict2}
print(merged_dict)

max_value = max([10, 20, 30, 40, 50])
print("Max value:", max_value)

min_value = min([10, 20, 30, 40, 50])
print("Min value:", min_value)

total = sum([10, 20, 30, 40, 50])
print("Total sum:", total)

reversed_list = [10, 20, 30, 40, 50][::-1]
print("Reversed list:", reversed_list)

cubes = [x**3 for x in range(10)]
print("Cubes:", cubes)

print(20 in [10, 20, 30, 40, 50])

list1 = [5, 10, 15]
list2 = [20, 25, 30]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

repeated_list = [5, 10, 15] * 2
print("Repeated list:", repeated_list)

print("Length of list:", len([5, 10, 15, 20, 25]))

print("First element:", [5, 10, 15, 20, 25][0])
print("Last element:", [5, 10, 15, 20, 25][-1])

my_list = [5, 10, 15, 20, 25]
my_list[1] = 12
print("Modified list:", my_list)

del my_list[1]
print("List after deletion:", my_list)

my_list.insert(1, 10)
print("List after insertion:", my_list)

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

my_list.clear()
print("List after clearing:", my_list)

courses = {
    "Math": {"Teacher": "Mr. Smith", "Students": ["John", "Alice", "Bob"]},
    "Science": {"Teacher": "Mrs. Johnson", "Students": ["Mike", "Sara", "Tom"]},
}
print("Math teacher:", courses["Math"]["Teacher"])

default_dict = {}
default_dict["a"] = default_dict.get("a", 0) + 1
print("Default dictionary:", default_dict)

items = ["apple", "banana", "cherry"]
indexed_items = list(enumerate(items))
print("Indexed items:", indexed_items)

keys = ["one", "two", "three"]
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))
print("Combined dictionary:", combined_dict)

counter = 1
print("Next counter value:", counter)
counter += 2
print("Next counter value:", counter)

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
largest = sorted(numbers)[-3:]
smallest = sorted(numbers)[:3]
print("Three largest numbers:", largest)
print("Three smallest numbers:", smallest)


def multiply(x, y):
    return x * y


double = lambda y: multiply(2, y)
print("Double 5:", double(5))

elements = ["a", "b", "c", "a", "b", "a"]
counter = {}
for element in elements:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1
print("Element frequencies:", counter)

iterable1 = [1, 2, 3]
iterable2 = ["a", "b", "c"]
combined = iterable1 + iterable2
print("Chained iterable:", combined)

Point = lambda x, y: (x, y)
point = Point(1, 2)
print("Point:", point)

deq = [1, 2, 3]
deq.append(4)
deq.insert(0, 0)
print("Deque after append:", deq)
deq.pop()
deq.pop(0)
print("Deque after pop:", deq)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined_dict = {**dict1, **dict2}
print("Combined dictionary:", combined_dict)

arr = [1, 2, 3, 4, 5]
print("Array:", arr)

sorted_list = [1, 3, 4, 7]
sorted_list.insert(2, 5)
print("Sorted list after insertion:", sorted_list)
print("Position of 5 in sorted list:", sorted_list.index(5))

cycle_iterator = ["A", "B", "C"]
print("Next cycle value:", cycle_iterator[0])
print("Next cycle value:", cycle_iterator[1])

numbers = [1, 2, 3, 4]
product = 1
for number in numbers:
    product *= number
print("Product of list:", product)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci of 6 is:", fibonacci(6))

x = 50
y = 70
z = x + y
print("The sum is:", z)

age = 21
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

for i in range(7):
    print("Number:", i)

count = 7
while count > 0:
    print("Count:", count)
    count -= 1

def square_root(n):
    return n ** 0.5
result = square_root(16)
print("Square root of 16 is:", result)

numbers = [10, 20, 30, 40, 50]
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print("Sum of numbers:", sum_numbers)

person = {"name": "Charlie", "age": 35, "city": "Los Angeles"}
print(person["name"], "is", person["age"], "years old.")

first_name = "Emily"
last_name = "Clark"
full_name = first_name + " " + last_name
print("Full name:", full_name)

name = input("Enter your name: ")
print("Hello,", name)

a = 25
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

num = 12
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print("Max of 10, 20, and 30 is:", max_of_three(10, 20, 30))

text = "python"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

def is_palindrome(s):
    return s == s[::-1]
print("Is 'madam' a palindrome?", is_palindrome("madam"))

prime_numbers = [x for x in range(20) if all(x % y != 0 for y in range(2, x))]
print("Prime numbers:", prime_numbers)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"The {self.breed} named {self.name} barks.")
dog = Dog("Buddy", "Golden Retriever")
dog.bark()

with open("data.txt", "w") as file:
    file.write("Data example")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

try:
    result = int("123")
    print("Valid number!")
except ValueError:
    print("Invalid number!")

my_tuple = (10, 20, 30, 40)
print(my_tuple[2])

my_set = {100, 200, 300, 400}
my_set.add(500)
print(my_set)

numbers = [100, 200, 300, 400, 500]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

sum_numbers = 0
for num in numbers:
    sum_numbers += num
print(sum_numbers)

multiply = lambda x, y: x * y
print(multiply(7, 8))

for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 6 is:", factorial(6))

my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])

squared_numbers = {x: x * x for x in range(10)}
print(squared_numbers)

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"The {self.color} cat named {self.name} meows.")
cat = Cat("Whiskers", "black")
cat.meow()

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

greeting = "Hello, {}. Welcome to {}."
print(greeting.format("Charlie", "Python"))

students = {"Alice": {"age": 25, "grade": "A"}, "Bob": {"age": 22, "grade": "B"}}
print(students["Bob"]["grade"])

a, b = b, a
print("a:", a, "b:", b)

my_list = list(range(20))
print(my_list[5:10])
print(my_list[:5])
print(my_list[15:])
print(my_list[::3])
print(my_list[::-2])

squared_even_numbers = [x * x for x in range(20) if x % 2 == 0]
print(squared_even_numbers)

matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

squared_numbers_dict = {x: x * x for x in range(20) if x % 2 == 0}
print(squared_numbers_dict)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

max_value = max([10, 20, 30, 40, 50])
print("Max value:", max_value)

min_value = min([10, 20, 30, 40, 50])
print("Min value:", min_value)

total = sum([10, 20, 30, 40, 50])
print("Total sum:", total)

reversed_list = [10, 20, 30, 40, 50][::-1]
print("Reversed list:", reversed_list)

squares = [x * x for x in range(20)]
print("Squares:", squares)

print(30 in [10, 20, 30, 40, 50])

list1 = [5, 10, 15]
list2 = [20, 25, 30]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

repeated_list = [5, 10, 15] * 2
print("Repeated list:", repeated_list)

print("Length of list:", len([5, 10, 15, 20, 25]))

print("First element:", [5, 10, 15, 20, 25][0])
print("Last element:", [5, 10, 15, 20, 25][-1])

my_list = [5, 10, 15, 20, 25]
my_list[0] = 10
print("Modified list:", my_list)

del my_list[0]
print("List after deletion:", my_list)

my_list.insert(0, 5)
print("List after insertion:", my_list)

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

my_list.clear()
print("List after clearing:", my_list)

a = 15
b = 25
c = a + b
print("The total is:", c)

user_age = 17
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

for num in range(3):
    print("Current number:", num)

counter = 4
while counter > 0:
    print("Counter value:", counter)
    counter -= 1

def cube_root(n):
    return n ** (1/3)
output = cube_root(27)
print("Cube root of 27 is:", output)

values = [5, 10, 15, 20, 25]
total_sum = 0
for value in values:
    total_sum += value
print("Total sum of values:", total_sum)

employee = {"name": "John", "age": 28, "department": "Engineering"}
print(employee["name"], "works in", employee["department"])

first = "Sarah"
last = "Johnson"
full = first + " " + last
print("Full name:", full)

username = input("Enter your username: ")
print("Welcome,", username)

x = 12
y = 4
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)
print("Remainder:", x % y)

number = 14
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

def min_of_three(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
print("Min of 15, 10, and 20 is:", min_of_three(15, 10, 20))

word = "programming"
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

def is_palindrome(s):
    return s == s[::-1]
print("Is 'noon' a palindrome?", is_palindrome("noon"))

multiples_of_three = [x for x in range(20) if x % 3 == 0]
print("Multiples of three:", multiples_of_three)

class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def chirp(self):
        print(f"The {self.species} named {self.name} chirps.")
bird = Bird("Tweety", "Canary")
bird.chirp()

with open("notes.txt", "w") as file:
    file.write("This is a note.")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

try:
    result = 100 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")

my_tuple = (15, 25, 35, 45)
print(my_tuple[1])

my_set = {1000, 2000, 3000}
my_set.add(4000)
print(my_set)

numbers = [1000, 2000, 3000, 4000]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)

total = 0
for num in numbers:
    total += num
print("Total:", total)

multiply = lambda x, y: x * y
print("Product of 9 and 7:", multiply(9, 7))

for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print("3 to the power of 4 is:", power(3, 4))

my_list = [11, 22, 33, 44, 55]
print(my_list[2:4])

cubed_numbers = {x: x ** 3 for x in range(10)}
print("Cubed numbers:", cubed_numbers)

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"This vehicle is a {self.make} {self.model}.")
vehicle = Vehicle("Ford", "Mustang")
vehicle.display()

fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
print(fruits)
fruits.remove("banana")
print(fruits)

message = "Hi, {}. Welcome to {}."
print(message.format("John", "Programming"))

employees = {
    "Alice": {"age": 30, "position": "Manager"},
    "Bob": {"age": 25, "position": "Developer"},
}
print(employees["Alice"]["position"])

x, y = y, x
print("x:", x, "y:", y)

my_list = list(range(30))
print(my_list[10:15])
print(my_list[:10])
print(my_list[20:])
print(my_list[::5])
print(my_list[::-3])

squared_odd_numbers = [x ** 2 for x in range(20) if x % 2 != 0]
print("Squared odd numbers:", squared_odd_numbers)

matrix = [[i + j for j in range(4)] for i in range(4)]
print(matrix)

cubed_odd_numbers = {x: x ** 3 for x in range(20) if x % 2 != 0}
print("Cubed odd numbers:", cubed_odd_numbers)

dict1 = {"x": 100, "y": 200}
dict2 = {"y": 300, "z": 400}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

max_val = max([100, 200, 300, 400, 500])
print("Max value:", max_val)

min_val = min([100, 200, 300, 400, 500])
print("Min value:", min_val)

total_sum = sum([100, 200, 300, 400, 500])
print("Total sum:", total_sum)

reversed_list = [100, 200, 300, 400, 500][::-1]
print("Reversed list:", reversed_list)

cubes = [x ** 3 for x in range(10)]
print("Cubes:", cubes)

print(50 in [10, 20, 30, 40, 50])

list1 = [15, 25, 35]
list2 = [45, 55, 65]
combined = list1 + list2
print("Combined list:", combined)

repeated = [15, 25, 35] * 2
print("Repeated list:", repeated)

print("Length of list:", len([15, 25, 35, 45, 55]))

print("First element:", [15, 25, 35, 45, 55][0])
print("Last element:", [15, 25, 35, 45, 55][-1])

my_list = [15, 25, 35, 45, 55]
my_list[1] = 30
print("Modified list:", my_list)

del my_list[1]
print("List after deletion:", my_list)

my_list.insert(1, 25)
print("List after insertion:", my_list)

popped = my_list.pop()
print("Popped element:", popped)
print("List after popping:", my_list)

my_list.clear()
print("List after clearing:", my_list)

p = 100
q = 200
r = p + q
print("The result is:", r)

user_age = 22
if user_age >= 21:
    print("You are allowed to enter.")
else:
    print("You are not allowed to enter.")

for i in range(6):
    print("Iteration:", i)

timer = 5
while timer > 0:
    print("Time left:", timer)
    timer -= 1

def square(n):
    return n ** 2
result = square(9)
print("Square of 9 is:", result)

data = [3, 6, 9, 12, 15]
total = 0
for item in data:
    total += item
print("Total of data:", total)

profile = {"name": "Emma", "age": 24, "city": "Chicago"}
print(profile["name"], "lives in", profile["city"])

first_name = "Michael"
last_name = "Brown"
full_name = first_name + " " + last_name
print("Full name:", full_name)

user = input("Enter your username: ")
print("Hello,", user)

m = 20
n = 5
print("Sum:", m + n)
print("Difference:", m - n)
print("Product:", m * n)
print("Quotient:", m / n)
print("Remainder:", m % n)

value = 17
if value % 2 == 0:
    print(value, "is even.")
else:
    print(value, "is odd.")

def max_of_four(a, b, c, d):
    return max(a, b, c, d)
print("Max of 10, 20, 30, 40 is:", max_of_four(10, 20, 30, 40))

text = "algorithm"
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

def is_palindrome(s):
    return s == s[::-1]
print("Is 'deified' a palindrome?", is_palindrome("deified"))

multiples_of_five = [x for x in range(50) if x % 5 == 0]
print("Multiples of five:", multiples_of_five)

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def swim(self):
        print(f"The {self.species} named {self.name} is swimming.")
fish = Fish("Nemo", "Clownfish")
fish.swim()

with open("log.txt", "w") as file:
    file.write("Log entry.")

with open("log.txt", "r") as file:
    content = file.read()
    print(content)

try:
    result = int("456")
    print("Valid integer!")
except ValueError:
    print("Invalid integer!")

my_tuple = (50, 100, 150, 200)
print(my_tuple[2])

my_set = {500, 1000, 1500}
my_set.add(2000)
print(my_set)

numbers = [500, 1000, 1500, 2000]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

total = 0
for num in numbers:
    total += num
print("Total:", total)

multiply = lambda x, y: x * y
print("Product of 8 and 9:", multiply(8, 9))

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 7 is:", factorial(7))

my_list = [10, 20, 30, 40, 50]
print(my_list[1:3])

cubed_numbers = {x: x ** 3 for x in range(10)}
print("Cubed numbers:", cubed_numbers)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"The book '{self.title}' is written by {self.author}.")
book = Book("1984", "George Orwell")
book.display()

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

greeting = "Hello, {}. Welcome to {}."
print(greeting.format("Emma", "Library"))

employees = {
    "Alice": {"age": 30, "position": "Manager"},
    "Bob": {"age": 25, "position": "Developer"},
}
print(employees["Bob"]["position"])

a, b = b, a
print("a:", a, "b:", b)

my_list = list(range(50))
print(my_list[10:20])
print(my_list[:10])
print(my_list[40:])
print(my_list[::10])
print(my_list[::-5])

squared_even_numbers = [x ** 2 for x in range(50) if x % 2 == 0]
print("Squared even numbers:", squared_even_numbers)

matrix = [[i * j for j in range(5)] for i in range(5)]
print(matrix)

cubed_even_numbers = {x: x ** 3 for x in range(50) if x % 2 == 0}
print("Cubed even numbers:", cubed_even_numbers)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

max_val = max([100, 200, 300, 400, 500])
print("Max value:", max_val)

min_val = min([100, 200, 300, 400, 500])
print("Min value:", min_val)

total_sum = sum([100, 200, 300, 400, 500])
print("Total sum:", total_sum)

reversed_list = [100, 200, 300, 400, 500][::-1]
print("Reversed list:", reversed_list)

cubes = [x ** 3 for x in range(10)]
print("Cubes:", cubes)

print(100 in [10, 20, 30, 40, 50])

list1 = [15, 25, 35]
list2 = [45, 55, 65]
combined = list1 + list2
print("Combined list:", combined)

repeated = [15, 25, 35] * 2
print("Repeated list:", repeated)

print("Length of list:", len([15, 25, 35, 45, 55]))

print("First element:", [15, 25, 35, 45, 55][0])
print("Last element:", [15, 25, 35, 45, 55][-1])

my_list = [15, 25, 35, 45, 55]
my_list[1] = 30
print("Modified list:", my_list)

del my_list[1]
print("List after deletion:", my_list)

my_list.insert(1, 25)
print("List after insertion:", my_list)

popped = my_list.pop()
print("Popped element:", popped)
print("List after popping:", my_list)

my_list.clear()
print("List after clearing:", my_list)
