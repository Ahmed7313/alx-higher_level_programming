#!/usr/bin/python3
output = []
for i in range(97, 123):  # ASCII values for 'a' to 'z'
    if i != 101 and i != 113:  # Excluding 'e' and 'q'
        output.append(chr(i))
print("{}".format(''.join(output)), end='')
