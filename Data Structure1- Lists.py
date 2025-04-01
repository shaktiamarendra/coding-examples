# This Python Program showcases basic access of lists of various entities like tuples, dictionaries and sets

# 1: Define a list of tuples
data = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Designer"),
    ("Charlie", 35, "Manager"),
    ("Diana", 28, "Data Scientist")
]

# Display the list of tuples
print("List of tuples:")
print(f"Type of Data is: {type(data)}")

for item in data:
    print(f"Type of Data is: {type(item)}")
    print(item)

# Display each element in the tuples
print("\nDetailed breakdown:")
for name, age, profession in data:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
print("-" * 30)

# 2: Define a list of dictionaries
data = [
    {"Name": "Alice", "Age": 25, "Profession": "Engineer"},
    {"Name": "Bob", "Age": 30, "Profession": "Designer"},
    {"Name": "Charlie", "Age": 35, "Profession": "Manager"},
    {"Name": "Diana", "Age": 28, "Profession": "Data Scientist"}
]

# Display the list of dictionaries
print("List of dictionaries:")
for item in data:
    print(f"Type of Data is: {type(item)}")
    print(item)
print("-" * 20)

# Display each dictionary's key-value pairs in detail
print("\nDetailed breakdown:")
for item in data:
    for key, value in item.items():
        print(f"Type of Data is: {type(item.items())}")
        print(f"{key}: {value}")
    print("-" * 20)

# 3: Define a list of sets
data = [
    {"Name: Alice", "25", "Profession: Engineer"},
    {"Bob", "30", "Profession: Designer", "30"},
    {"Name: Davis", "Age: 35", "Profession: Manager"},
    {"Name: Diana","Data", "Age: 28", "Data"}
]

# Display the list of sets
print("List of Sets:")
for item in data:
    print(f"Type of Data is: {type(item)}")
    print(item)
print("-" * 20)

# Display each dictionary's key-value pairs in detail
print("\nDetailed breakdown:")
# Print individual elements of each set
print("\nDetailed breakdown (individual elements of the set):")
for item in data:
    print(f"Set: {item}")
    for element in item:
        print(f"Element: {element}")
    print("-" * 20)

#4: Define an array of numbers to store temperatures
List_Numbers=[25.5, 27.3, 23.8, 26.1, 24.9, 22.7, 28.5]
# Function to display the list of numbers
def display_nums():
    for idx, s in enumerate(List_Numbers):
        print(f"Number {idx + 1}: {s}")

# Calling the function to display the sets
display_nums()

## Operations with List of Numbers
print(f"Temperature at 0th index is: {List_Numbers[0]}")
print(f"Temperature at 3rd index is: {List_Numbers[3]}")
List_Numbers[2]=24.2
print(f"Length of temperature array is: {len(List_Numbers)}")