"""
6.17 LAB: Swapping variables
Define a function named swap_values that takes four integers as parameters and swaps the first with the second, and the third with the fourth values. Then write a main program that reads four integers from input, calls function swap_values() to swap the values, and prints the swapped values on a single line separated with spaces.

Ex: If the input is:

3
8
2
4
function swap_values() returns and the main program outputs:

8 3 4 2
The program must define and call the following function.
def swap_values(user_val1, user_val2, user_val3, user_val4)
"""
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())
    
    user_val1, user_val2, user_val3, user_val4 = swap_values(user_val1, user_val2, user_val3, user_val4)
    
    print(user_val1, user_val2, user_val3, user_val4)