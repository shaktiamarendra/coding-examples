# Hash Table Class Definition
class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return (hash(key) % self.size)
    
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for item in bucket:
            print(f"Item: {item} of Bucket: {bucket}")
            if item[0]==key: #This part of the function ensures that duplicate keys are not inserted. Instead, it updates the value of the existing key if it's already in the hash table.
                print(f"Item[0] is {item[0]}")
                item[1]=value
                return
        bucket.append((key, value)) 
    
    def get(self, key):
        index=self.hash_function(key)
        bucket = self.buckets[index]
        for item in bucket:
            if item[0]== key:
                return item[1]
        return None

    def display(self):
        for index, bucket in enumerate (self.buckets):
            print("Bucket", index)
            for item in bucket:
                print(item)

#Create an instance of the Hash Table
student_ages = HashTable(size=4)

#Create key-value pairs into the Hash Table
student_ages.insert("Ram","56")
student_ages.insert("Shyam", "45")
student_ages.insert("Laxman","48")
student_ages.insert("Balram", "47")
student_ages.insert("Bharat","50")
student_ages.insert("Shatrughan", "44")

# Retrieve values based on keys from the Hash Table
age=student_ages.get("Sarah")
print("Sarah's age is:", age)

age=student_ages.get("Shyam")
print("Shyam's age is:", age)

# Display the Hash table
student_ages.display()