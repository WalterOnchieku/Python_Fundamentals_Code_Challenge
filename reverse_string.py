def reverse_string():
    # Prompt the user for input and store it in the variable 'txt'
    txt = input("Type here: ")
    
    # Return the reverse of the string using slicing [::-1]
    return txt[::-1]

# Call the reverse_string function and print the reversed string
print(reverse_string())