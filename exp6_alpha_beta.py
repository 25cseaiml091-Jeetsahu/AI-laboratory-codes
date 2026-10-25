import math
def minimax(depth, node_index, is_max, scores, alpha, beta, max_depth):
    if depth == max_depth:
        return scores[node_index]
    if is_max:
        max_eval = -math.inf
        for i in range(2):
            eval = minimax(depth + 1, node_index * 2 + i, False, scores, alpha, beta, max_depth)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval = minimax(depth + 1, node_index * 2 + i, True, scores, alpha, beta, max_depth)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
if __name__ == '__main__':
    scores_input = input("Enter 8 leaf node values separated by space: ")
    scores = list(map(int, scores_input.split()))
    if len(scores) != 8:
        print("Error: Please enter exactly 8 values.")
    else:
        max_depth = int(math.log2(len(scores)))
        optimal_value = minimax(0, 0, True, scores, -math.inf, math.inf, max_depth)
        print("The optimal value is:", optimal_value)
    """ OUTPUT: 
    Enter 8 leaf node values separated by space: 3 5 6 9 1 2 0 -1
    The optimal value is: 5 """
