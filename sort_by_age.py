def sort_by_age(tup):
    # Get the length of the list of tuples
    lst = len(tup)
    
    # Outer loop to iterate over the entire list
    for i in range(0, lst):
        # Inner loop for the comparison of adjacent elements
        for j in range(0, lst - i - 1):
            # Compare the ages (second element of the tuples)
            if tup[j][1] > tup[j + 1][1]:
                # Swap the tuples if they are in the wrong order
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    
    # Return the sorted list of tuples
    return tup

# Example list of tuples with names and ages
tup = [('Walter', 24), ('Nelson', 10), ('Vera', 28), ('Jackie', 5), ('Chuck', 20), ('Bryce', 15)]

# Print the sorted list of tuples
print(sort_by_age(tup))
