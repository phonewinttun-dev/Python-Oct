# def greet():
#     print("Hello! Welcome to Python Functions.")

# greet()


# def greet_user(name):  # define function with parameter
#     print(f"Hello, {name}!")


# greet_user("Ko Khun")  # call function with argument
# greet_user("Ma Shun")  # call function with argument


# def add_numbers(num1, num2):
#     print(f"{num1} + {num2} = {num1 + num2}")


# # sum(5, 10)
# add_numbers(10, 10)


# def introduce(name, country="Myanmar"):
#     print(f"My name is {name} and I am from {country}.")


# introduce("Min Min")
# introduce("John", "Singapore")


# def multiply(a, b):
#     return a * b


# # return -> 1. create variable, 2. call function, 3. store return value in variable, 4. use variable
# result = multiply(4, 5)
# print(f"The result is: {result}")


def is_even(number):
    return number % 2 == 0


print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")


# def calculate_box(length, width, height):
#     return 2 * (length + width), length * width, length * width * height


# p, a, v = calculate_box(5, 3, 2)
# print(f"Perimeter: {p}, Area: {a}, Volume: {v}")
