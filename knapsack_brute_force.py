import time

def knapsack_brute_force(values, weights, capacity):
    num_items = len(values)
    max_value = 0
    best_combination = []

    for i in range(2**num_items):
        combination = []
        total_value = 0
        total_weight = 0

        for j in range(num_items):
            if (i >> j) & 1:
                combination.append(j)
                total_value += values[j]
                total_weight += weights[j]

        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = combination

    return max_value, best_combination


# Example usage
values = [10, 12, 8, 15]
weights = [2, 4, 6, 9]
capacity = 15

start_time = time.time()
max_value, best_combination = knapsack_brute_force(values, weights, capacity)
end_time = time.time()

execution_time = end_time - start_time

print("Best combination of items:", best_combination)
print("Total value:", max_value)
print("Execution time:", execution_time, "seconds")
