def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # recursion
        else:
            flat_list.append(item)
    return flat_list

# Example usage
nested = [1, [2, [3, 4], 5], 6]
print(flatten_list(nested))  # Output: [1, 2, 3, 4, 5, 6]
