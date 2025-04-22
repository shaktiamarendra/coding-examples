#Python implementation of the Trie Data Structure (also known as a prefix tree). A trie is particularly useful for problems involving strings, such as searching for prefixes, autocomplete, and dictionary implementations.
class TrieNode:
    def __init__(self):
        # Each TrieNode contains a dictionary of children and a flag to mark the end of a word
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # The root of the Trie
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        current_node = self.root
        for char in word:
            # If the character is not already in the current node's children, add it
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Move to the next node
            current_node = current_node.children[char]
        # Mark the end of the word
        current_node.is_end_of_word = True

    def search(self, word):
        """
        Search for a word in the Trie.
        Returns True if the word exists, otherwise False.
        """
        current_node = self.root
        for char in word:
            # If the character is not in the current node's children, the word doesn't exist
            if char not in current_node.children:
                return False
            # Move to the next node
            current_node = current_node.children[char]
        # Return True only if the end of the word is marked
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if any word in the Trie starts with the given prefix.
        Returns True if such a prefix exists, otherwise False.
        """
        current_node = self.root
        for char in prefix:
            # If the character is not in the current node's children, the prefix doesn't exist
            if char not in current_node.children:
                return False
            # Move to the next node
            current_node = current_node.children[char]
        return True


# Example Usage
if __name__ == "__main__":
    trie = Trie()

    # Insert words into the trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    trie.insert("bat")

    # Search for words
    print(trie.search("apple"))  # True
    print(trie.search("app"))    # True
    print(trie.search("appl"))   # False

    # Check prefixes
    print(trie.starts_with("app"))  # True
    print(trie.starts_with("bat"))  # True
    print(trie.starts_with("cat"))  # False