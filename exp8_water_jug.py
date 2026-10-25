from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    queue = deque([((0, 0), [(0, 0)])])
    visited = set()
    visited.add((0, 0))
    while queue:
        (j1, j2), path = queue.popleft()
        if j1 == target or j2 == target:
            print("Steps to solve the Water Jug problem:")
            for state in path:
                print(state)
            return
        rules = [
            (jug1_capacity, j2),                                                  # Fill Jug 1
            (j1, jug2_capacity),                                                  # Fill Jug 2
            (0, j2),                                                              # Empty Jug 1
            (j1, 0),                                                              # Empty Jug 2
            (j1 - min(j1, jug2_capacity - j2), j2 + min(j1, jug2_capacity - j2)), # Pour Jug 1 -> Jug 2
            (j1 + min(j2, jug1_capacity - j1), j2 - min(j2, jug1_capacity - j1))  # Pour Jug 2 -> Jug 1
        ]
        for state in rules:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    print("No solution possible.")
if __name__ == '__main__':
    jug1 = int(input("Enter Jug 1 Capacity: "))
    jug2 = int(input("Enter Jug 2 Capacity: "))
    target = int(input("Enter Target Capacity: "))
    water_jug_bfs(jug1, jug2, target)
""" OUTPUT:
Enter Jug 1 Capacity: 4
Enter Jug 2 Capacity: 3
Enter Target Capacity: 2
Steps to solve the Water Jug problem:
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2) """
