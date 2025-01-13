from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_shortest_path(self, start, target):
        visited = [False] * self.vertices
        parent = [-1] * self.vertices  # Store the parent of each node
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()

            # Check if we've reached the target node
            if node == target:
                path = []
                while node != -1:
                    path.append(node)
                    node = parent[node]
                return path[::-1]  # Return reversed path
        
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        return None  # No path found

# Example usage:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

path = g.bfs_shortest_path(0, 5)
print("Shortest path from 0 to 5:", path)