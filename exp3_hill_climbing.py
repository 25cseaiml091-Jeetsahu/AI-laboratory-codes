def objective_function(x):
    return -(x ** 2) + 5
def hill_climbing(start, step_size, max_iterations):
    current = start
    current_value = objective_function(current)
    for i in range(max_iterations):
        neighbors = [current + step_size, current - step_size]
        next_eval = -float('inf')
        next_position = None
        for n in neighbors:
            value = objective_function(n)
            if value > next_eval:
                next_eval = value
                next_position = n
        if next_eval > current_value:
            current = next_position
            current_value = next_eval
        else:
            break
    return current, current_value
if __name__ == '__main__':
    start = float(input("Enter starting position: "))
    step_size = float(input("Enter step size: "))
    max_iterations = int(input("Enter maximum iterations: "))
    best_position, max_value = hill_climbing(start, step_size, max_iterations)
    print(f"Best position: {best_position}")
    print(f"Maximum value: {max_value}")
"""OUTPUT:
Enter starting position: -2.0
Enter step size: 0.5
Enter maximum iterations: 10
Best position: 0.0
Maximum value: 5.0 """
