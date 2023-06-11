class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


def knapsack_branch_and_bound(values, weights, capacity):
    num_items = len(values)
    items = []
    for i in range(num_items):
        items.append(Item(values[i], weights[i]))

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    max_value = 0
    best_combination = []

    def branch_and_bound(node, current_value, current_weight):
        nonlocal max_value, best_combination

        # Check if the current node is promising
        if node < num_items and current_weight + items[node].weight <= capacity:
            current_value += items[node].value
            current_weight += items[node].weight

            # Update the best solution if it's better than the current best
            if current_value > max_value:
                max_value = current_value
                best_combination = [i for i in range(node + 1)]

            # Explore the left child (with the current item)
            branch_and_bound(node + 1, current_value, current_weight)

            # Revert the changes for exploring the right child (without the current item)
            current_value -= items[node].value
            current_weight -= items[node].weight

            # Explore the right child (without the current item)
            branch_and_bound(node + 1, current_value, current_weight)

    branch_and_bound(0, 0, 0)

    return max_value, best_combination


# Example usage
values = [10, 12, 8, 15]
weights = [2, 4, 6, 9]
capacity = 15

max_value, best_combination = knapsack_branch_and_bound(values, weights, capacity)

print("Best combination of items:", best_combination)
print("Total value:", max_value)
