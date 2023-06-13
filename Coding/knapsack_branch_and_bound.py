import time 

class Item: 
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


def knapsack_branch_and_bound(values, weights, capacity): # O(n log n)
    num_items = len(values) 
    items = [] 
    for i in range(num_items):
        items.append(Item(values[i], weights[i]))

    items.sort(key=lambda x: x.ratio, reverse=True)

    max_value = 0
    best_combination = [] 

    def branch_and_bound(node, current_value, current_weight): # O(2^n)
        nonlocal max_value, best_combination

        if node < num_items and current_weight + items[node].weight <= capacity:
            current_value += items[node].value
            current_weight += items[node].weight

            if current_value > max_value:
                max_value = current_value
                best_combination = [i for i in range(node + 1)]

            branch_and_bound(node + 1, current_value, current_weight)

            current_value -= items[node].value
            current_weight -= items[node].weight

            branch_and_bound(node + 1, current_value, current_weight)

    branch_and_bound(0, 0, 0)

    return max_value, best_combination


# Example usage
values = [10, 12, 8, 15]
weights = [2, 4, 6, 9]
capacity = 15

start_time = time.time()  
max_value, best_combination = knapsack_branch_and_bound(values, weights, capacity) 
end_time = time.time() 

execution_time = end_time - start_time

print("Best combination of items:", best_combination)
print("Total value:", max_value)
print("Execution time:", execution_time, "seconds")
