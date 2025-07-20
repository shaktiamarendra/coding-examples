"""
Build a small, practical Python app that searches through a text file containing a list of names and surnames, and prints out all the full names that have a specific given name (the first word in each line).

But this time, instead of making your own text file, you’ll use a real dataset provided for you.
It’s a simple .txt file hosted on Google Drive

Break this problem into simple steps:

1- Open the text file using Python’s with open(...) as f: pattern so it handles closing automatically.

2- Read each line in the file. Use .strip() to remove newline characters.

3- Split the line into words using .split(). That way, you can check the first word (the given name).

4-Compare the first word to the name the user entered.

5- Use .lower() on both to make the comparison case-insensitive.

6- If it matches, store the entire line in a list.

7- After going through all lines, print out all the matches — or a message if none are found.
"""

def get_given_name():
    """Prompt the user for a given name to search for."""
    userName=input("Enter the given name to search for: ")
    matches=match_given_name(userName)
    if matches:
        print("Found the following matches:")
        for match in matches:
            print(match)
    else:
        print("No matches found.")
    
def match_given_name(given_name):
    matches = []
    with open("names.txt") as f:
       for line in f:
           print(f"Stream from file: {line}")
           line = line.strip()
           print(f"Stripped line: {line}")
           if line:
               words = line.split()
               print(f"Split words: {words}")
               first_name = words[0]
               print(f"First name: {first_name}")
               if first_name.lower() == given_name.lower():
                   matches.append(line)
    return matches

if __name__ == "__main__":
    get_given_name()