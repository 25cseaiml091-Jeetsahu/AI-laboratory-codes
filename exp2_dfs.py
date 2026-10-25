def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
# Graph representation
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f', 'g'],
    'e': ['f'],
    'f': ['g'],
    'g': []
}
if __name__ == '__main__':
    visited = set()
    print("DFS Traversal order :", end=" ")
    dfs(visited, graph, 'a')
  """OUTPUT:  
  Following is the Breadth-First Search:
        A B C D E F """
