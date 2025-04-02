from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        V = len(adj) # Number of vertices
        visited = [False] * V # Visited array to track Visited nodes
        bfs_result = [] # List to store BFS Traversal

        # Queue for BFS
        queue = deque([0])
        visited[0] = True

        while queue:
            node = queue.popleft()
            bfs_result.append(node)
            
            # Traverse all the adjacent nodes in the given order
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return bfs_result

# Taking user input for adjacency list
def get_input():
    V = int(input("Enter number of vertices: "))
    adj = []
    for i in range(V):
        neighbors = list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
        adj.append(neighbors)
    return adj

# Running BFS traversal
if __name__ == "__main__":
    adj_list = get_input()
    solution = Solution()
    print("BFS Traversal:", solution.bfs(adj_list))
