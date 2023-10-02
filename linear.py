def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

# Sample list of products
products = ["Apple", "Banana", "Apple", "Orange", "Grapes", "Apple"]

# Target product to search for
target_product = "Apple"

# Call the function to find all occurrences of "Apple"
result = linear_search_product(products, target_product)

# Check if the result is empty (product not found) or contains indices
if len(result) > 0:
    print("Indices of occurrences of", target_product, ":", result)
else:
    print(target_product, "not found in the list of products.")
