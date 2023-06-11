def knapsack_brute_force(values, weights, capacity):
    num_items = len(values)
    max_value = 0
    best_combination = []

    # Generate all possible combinations of items
    for i in range(2**num_items):
        combination = []
        total_value = 0
        total_weight = 0

        # Check each bit of the binary representation
        for j in range(num_items):
            if (i >> j) & 1:
                combination.append(j)
                total_value += values[j]
                total_weight += weights[j]

        # Update the best combination if it is valid and has the maximum value
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = combination

    return max_value, best_combination


# Example usage
values = [10, 12, 8, 15]
weights = [2, 4, 6, 9]
capacity = 15

max_value, best_combination = knapsack_brute_force(values, weights, capacity)

print("Best combination of items:", best_combination)
print("Total value:", max_value)
