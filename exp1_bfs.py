from collections import deque
def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited.append(start)
    while queue:
        m = queue.popleft()
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
if __name__ == '__main__':
    print("Following is the Breadth-First Search:")
    bfs(graph, 'A')
   """OUTPUT:
   Following is the Breadth-First Search:
    A B C D E F """
