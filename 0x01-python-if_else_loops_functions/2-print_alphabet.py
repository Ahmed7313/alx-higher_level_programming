#!/usr/bin/python3

# Initialize an empty string to accumulate alphabet characters
alphabet = ""

# Loop through ASCII values of lowercase letters and add them to the string
for i in range(97, 123):
    alphabet += chr(i)

# Use .format() to format the final string
print("{}".format(alphabet), end='')
