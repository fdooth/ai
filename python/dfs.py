class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list representation of the graph

    # Add an undirected edge between u and v
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Iterative DFS using a stack
    def dfs_stack(self, start):
        visited = [False] * self.vertices  # Keep track of visited nodes
        stack = [start]  # Initialize stack with the start node
        
        while stack:
            node = stack.pop()  # Pop a node from the stack
            
            if not visited[node]:
                visited[node] = True  # Mark the node as visited
                print(node, end=" ")  # Process the node (here we are printing it)
                
                # Push all unvisited neighbors to the stack (reverse order to ensure correct order of exploration)
                for neighbor in reversed(self.graph[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)

# Example usage
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("DFS (Stack-based) starting from node 0:")
g.dfs_stack(0)
print()