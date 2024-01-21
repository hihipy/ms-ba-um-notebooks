# This program includes a function that swaps the values of two pairs of integers,
# and a main program that reads four integers, uses the function to swap the values, 
# and prints the results.

def swap_values(user_val1, user_val2, user_val3, user_val4):
    """
    Swaps the first parameter with the second, and the third parameter with the fourth.
    
    Parameters:
    user_val1 (int): The first integer value.
    user_val2 (int): The second integer value.
    user_val3 (int): The third integer value.
    user_val4 (int): The fourth integer value.
    
    Returns:
    tuple: A tuple containing the swapped values.
    """
    # Swap the first and second values, as well as the third and fourth values, then return them.
    return user_val2, user_val1, user_val4, user_val3


# Check if the script is the main program and not being imported as a module.
if __name__ == '__main__':
    # Read four integer values from user input.
    user_val1 = int(input("Enter the first integer: "))
    user_val2 = int(input("Enter the second integer: ")) 
    user_val3 = int(input("Enter the third integer: "))
    user_val4 = int(input("Enter the fourth integer: "))

    # Call the swap_values function to swap the values.
    user_val1, user_val2, user_val3, user_val4 = swap_values(user_val1, user_val2, user_val3, user_val4)

    # Print the swapped values on a single line separated by spaces.
    print(user_val1, user_val2, user_val3, user_val4)
