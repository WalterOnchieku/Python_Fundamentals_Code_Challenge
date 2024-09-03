def count_vowels():
    # Prompt the user for input and store it in the variable 'txt'
    txt = input("Type here: ")
    
    # Define a string containing all vowels, both lowercase and uppercase
    vowels = "aeiouAEIOU"
    
    # Use a generator expression to count the occurrences of each vowel in the input string
    count = sum(txt.count(vowel) for vowel in vowels)
    
    # Return the total count of vowels
    return count

# Call the count_vowels function
count_vowels()