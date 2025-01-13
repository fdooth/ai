import copy
from heapq import heappush, heappop

n = 3

# bottom, left, top, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

# A class for Priority Queue
class priorityQueue:
    def __init__(self):
        self.heap = []

    # Inserts a new key 'k'
    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    # Method to know if the Queue is empty
    def empty(self):
        return not self.heap

# Node structure
class node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def calculateCost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] and mat[i][j] != final[i][j]:
                count += 1
    return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> node:
    # Copy data from parent matrix to current matrix
    new_mat = copy.deepcopy(mat)

    # Move tile by 1 position
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    # Set number of misplaced tiles
    cost = calculateCost(new_mat, final)

    # Create the new node
    return node(parent, new_mat, new_empty_tile_pos, cost, level)

# Function to print the N x N matrix
def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d " % mat[i][j], end=" ")
        print()

# Function to check if (x, y) is a valid matrix coordinate
def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

# Print path from root node to destination node
def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mat)
    print()

def solve(initial, empty_tile_pos, final):
    pq = priorityQueue()

    # Create the root node
    cost = calculateCost(initial, final)
    root = node(None, initial, empty_tile_pos, cost, 0)

    # Add root to list of live nodes
    pq.push(root)

    while not pq.empty():
        # Extract the minimum cost node
        minimum = pq.pop()

        # If minimum is the answer node
        if minimum.cost == 0:
            printPath(minimum)
            return

        # Generate all possible children
        for i in range(4):
            new_tile_pos = [
                minimum.empty_tile_pos[0] + row[i],
                minimum.empty_tile_pos[1] + col[i]
            ]
            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                # Create a child node
                child = newNode(
                    minimum.mat,
                    minimum.empty_tile_pos,
                    new_tile_pos,
                    minimum.level + 1,
                    minimum,
                    final,
                )
                # Add child to list of live nodes
                pq.push(child)

# Driver Code

# Initial configuration
# Value 0 is used for empty space
initial = [[1, 2, 3], 
           [5, 6, 0], 
           [7, 8, 4]]

# Solvable Final configuration
# Value 0 is used for empty space
final = [[1, 2, 3], 
         [5, 8, 6], 
         [0, 7, 4]]

# Blank tile coordinates in initial configuration
empty_tile_pos = [1, 2]

# Function call to solve the puzzle
solve(initial, empty_tile_pos, final)
