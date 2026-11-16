# while Loop
counter = 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1

number = 0
while number < 8:
    number += 1
    if number == 3:
        print(f"Skipping number {number} with continue")
        continue
    if number == 6:
        print(f"Stopping loop at number {number} with break")
        break
    print(f"Processed number: {number}")

# for loop
for i in range(1, 6):
    print(f"Counting: {i}")

print("Range with step:")
for value in range(10, 50, 10):
    print(f"Step value: {value}")

# for loop with list
cities = ["Yangon", "Mandalay", "Naypyidaw", "Taunggyi"]
for city in cities:
    print(f"City: {city}")

# for loop with string
keyword = "CODE"
for letter in keyword:
    print(f"Character: {letter}")

# for loop with dictionary
book_inventory = {
    "Python Basics": 15000,
    "Data Structures": 22000,
    "Database Systems": 18000,
}
for book_title, price in book_inventory.items():
    print(f"Book: {book_title} | Price: {price} MMK")

# for loop with break and continue
scores = [45, 78, 92, -1, 88, 60]
for score in scores:
    if score < 0:
        print("Invalid negative score found. Halting report.")
        break
    if score < 50:
        print(f"Score {score} is below passing mark (skipped).")
        continue
    print(f"Valid passing score: {score}")

# nested for loop
for row in range(1, 4):
    for col in range(1, 4):
        print(f"[{row},{col}]", end=" ")
    print()


colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"T-shirt: {color} | Size: {size}")
