"""
7.5 LAB: Palindrome
A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

palindrome: bob
Ex: If the input is:

bobby
the output is:

not a palindrome: bobby
Hint: Start by removing spaces. Then check if the string equals itself in reverse.
"""
# This program determines whether a given word or phrase is a palindrome.
# A palindrome is a sequence of characters that reads the same backward as forward.

# Prompt the user for a word or phrase and store the input.
s = input("Enter a word or phrase to check if it's a palindrome: ")

# Remove spaces from the input string and convert it to lowercase for uniformity in comparison.
# Spaces are removed to ensure that phrases can be checked as palindromes.
cleaned_string = s.replace(" ", "").lower()

# Check if the cleaned string is the same as its reverse.
# A palindrome will be identical to its reverse.
if cleaned_string == cleaned_string[::-1]:
    # If it is a palindrome, print the original string with the label "palindrome".
    print(f"palindrome: {s}")
else:
    # If it is not a palindrome, print the original string with the label "not a palindrome".
    print(f"not a palindrome: {s}")
