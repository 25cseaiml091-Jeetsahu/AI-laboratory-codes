import heapq
def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    visited = set()
    while open_list:
        f_score, g_score, current_node, path = heapq.heappop(open_list)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return path, g_score
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                new_g = g_score + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')
# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}
heuristics = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}
if __name__ == '__main__':
    start_node = 'A'
    goal_node = 'G'
    path, cost = a_star(graph, heuristics, start_node, goal_node)
    if path:
        print(f"shortest path: {'->'.join(path)}")
        print(f"total cost: {cost}")
    else:
        print("no path found")
""" OUTPUT:
shortest path: A->B->D->G
total cost: 6 """
