'''
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
'''

# Read the input string
s = input()

# Remove spaces and convert to lowercase for consistency
cleaned_string = s.replace(" ", "").lower()

# Check if string is the same as its reverse
if cleaned_string == cleaned_string[::-1]:
    print(f"palindrome: {s}")
else:
    print(f"not a palindrome: {s}")

