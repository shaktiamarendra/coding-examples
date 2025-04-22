# Define an array of numbers to store temperatures
List_Numbers=[25.5, 27.3, 23.8, 26.1, 24.9, 22.7, 28.5]
# Define an array of dictionaries to store name and roll no
List_Dictionaries = [
    {"shakti":2}, 
    {"vyakti":5}
    ]
# Define an array of tuples to store name, age and profession of employees which never changes
List_Tuples = [
    ("Name: Alice", "Age: 25", "Profession: Engineer"),
    ("Name: Bob", "Age: 30", "Profession: Designer"),
    ("Name: Charlie", "Age: 35", "Profession: Manager"),
    ("Name: Diana", "Age: 28", "Profession: Data Scientist")
]
# Define an array of sets to store mixed data
List_of_sets = [
    {1, 2, 3},
    {"apple", "banana", "cherry"},
    {True, False},
    {4.5, 6.7, 8.9},
    {"python", 3.9, "programming"},
    {10, 10, 340, 340}, #This has duplicate entries but only unique entries would be printed
    {"a", "b", "c"},
    {100, 200, 300, 400},
    {"x", "y", "z"},
    {10, 20, 30},
    {5, 10, 15, 20}
]
# Function to display the list of numbers
def display_nums():
    for idx, s in enumerate(List_Numbers):
        print(f"Number {idx + 1}: {s}")

# Calling the function to display the sets
display_nums()

# Function to display the list of dictionaries
def display_dicts():
    for idx, s in enumerate(List_Dictionaries):
        print(f"Dictionary {idx + 1}: {s}")

# Calling the function to display the dictionaries
display_dicts()

# Function to display the list of tuples
def display_tuples():
    for idx, s in enumerate(List_Tuples):
        print(f"Tuple {idx + 1}: {s}")

# Calling the function to display the tuples
display_tuples()

# Function to display the list of sets
def display_sets():
    for idx, s in enumerate(List_of_sets):
        print(f"Set {idx + 1}: {s}")

# Calling the function to display the sets
display_sets()

## Operations with List of Numbers
print(f"Temperature at 0th index is: {List_Numbers[0]}")
print(f"Temperature at 3rd index is: {List_Numbers[3]}")
List_Numbers[2]=24.2
print(f"Length of temperature array is: {len(List_Numbers)}")

# Operations with List of Dictionaries
for entit in List_Dictionaries:
    print(f"Printing individual attribute of the dictionary {entit}")
    for name, num in entit.items():
        print(f"Key: {name}")
        print(f"Value: {num}")

## Operations with List of Tuples
for i in range (len(List_Tuples)):
    print(f"Printing individual attribute of the tuple{i}")
    for j in range(len(List_Tuples[i])):
        print( List_Tuples [i][j] )