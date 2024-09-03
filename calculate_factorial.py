def calculate_factorial():
    # Prompt the user for input and convert it to an integer
    n = int(input("Enter a number: "))
    
    # Initialize the factorial variable to 1
    factorial = 1
    
    # Use a for loop to multiply the factorial variable by each number from 1 to n
    for i in range(1, n + 1):
        factorial *= i
    
    # Print the result, showing the factorial of the given number
    print(f"The factorial of {n} is {factorial}")
    
    # Return statement is optional here as there's no value being returned
    return

# Call the calculate_factorial function to execute the code
calculate_factorial()
