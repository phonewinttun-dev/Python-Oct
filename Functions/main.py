def greet():
    print("Hello! Welcome to Python Functions.")

greet()


def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user("Bob")


def add_numbers(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

add_numbers(5, 10)


def introduce(name, country="Myanmar"):
    print(f"My name is {name} and I am from {country}.")

introduce("Min Min")
introduce("John", "Singapore")


def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"The result is: {result}")


def is_even(number):
    return number % 2 == 0

print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")


def calculate_box(length, width, height):
    return 2 * (length + width), length * width, length * width * height

p, a, v = calculate_box(5, 3, 2)
print(f"Perimeter: {p}, Area: {a}, Volume: {v}")
