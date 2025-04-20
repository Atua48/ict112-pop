"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
original_string = "programming"
reversed_string = original_string[::-1]
print("reversed string:",reversed_string)
"""

2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name =input("Enter your full name:")
name_parts =full_name.split()
initials = "".join(part[0].upper() for part in name_parts)
print("initials:",initials+".")
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string = input("Enter string:")
processed_string = string.replace("","").lower()
if processed_string == processed_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}"is not a palindrome.')
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence =input("Enter sentence")
words = sentence.split()
words_count=len(words)
print("number of words in the sentence:",words_count)
"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
original_string = "This is a string and it is an example"
modified_string =original_string.replace("is","was")
print("modified string:",modified_string)