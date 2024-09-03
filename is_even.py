# function named is_even that takes a single parameter number and returns True if the number is even, and False otherwise
def is_even(number):
    # check if even by dividing by 2 to see if remainder is 0 or not
    if number % 2 == 0:
       return True
    else:
        return False
       
is_even(15)   