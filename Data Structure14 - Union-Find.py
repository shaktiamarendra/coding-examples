class UnionFind:
    def __init__(self, size):
        # Initialize the parent and rank arrays
        self.parent = [i for i in range(size)]  # Each node is its own parent initially
        self.rank = [0] * size  # Rank (or height) is initially 0 for all nodes

    def find(self, x):
        """
        Find the representative (root) of the set containing x.
        Uses path compression to make future queries faster.
        """
        if self.parent[x] != x:  # If x is not its own parent
            self.parent[x] = self.find(self.parent[x])  # Recursively find the root
        return self.parent[x]

    def union(self, x, y):
        """
        Union the sets containing x and y.
        Uses union by rank to keep the tree shallow.
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank: attach smaller tree under larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # Increase rank if both trees had the same rank

    def connected(self, x, y):
        """
        Check if x and y are in the same set.
        """
        return self.find(x) == self.find(y)


# Example Usage
if __name__ == "__main__":
    # Create a Union-Find structure with 10 elements (0 through 9)
    uf = UnionFind(10)

    # Union some elements
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)

    # Check if elements are connected
    print(uf.connected(1, 3))  # True
    print(uf.connected(1, 4))  # False

    # Find the representative (root) of a set
    print(uf.find(3))  # Should return the root of the set containing 3
    print(uf.find(5))  # Should return the root of the set containing 5