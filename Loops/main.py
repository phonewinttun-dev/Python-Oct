print("=== 1. Basic while Loop ===")
counter = 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1

print("\n=== 2. while Loop with break and continue ===")
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

print("\n=== 3. for Loop with range() ===")
for i in range(1, 6):
    print(f"Counting: {i}")

print("Range with step:")
for value in range(10, 50, 10):
    print(f"Step value: {value}")

print("\n=== 4. for Loop over a List ===")
cities = ["Yangon", "Mandalay", "Naypyidaw", "Taunggyi"]
for city in cities:
    print(f"City: {city}")

print("\n=== 5. for Loop with enumerate() ===")
languages = ["Python", "JavaScript", "C#", "SQL"]
for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")

print("\n=== 6. for Loop over a String ===")
keyword = "CODE"
for letter in keyword:
    print(f"Character: {letter}")

print("\n=== 7. for Loop over a Dictionary ===")
book_inventory = {
    "Python Basics": 15000,
    "Data Structures": 22000,
    "Database Systems": 18000,
}
for book_title, price in book_inventory.items():
    print(f"Book: {book_title} | Price: {price} MMK")

print("\n=== 8. for Loop with break and continue ===")
scores = [45, 78, 92, -1, 88, 60]
for score in scores:
    if score < 0:
        print("Invalid negative score found. Halting report.")
        break
    if score < 50:
        print(f"Score {score} is below passing mark (skipped).")
        continue
    print(f"Valid passing score: {score}")

print("\n=== 9. Nested Loops ===")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"[{row},{col}]", end=" ")
    print()
