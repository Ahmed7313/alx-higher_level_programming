#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i < j:
            if i < 8:  # To avoid printing a comma and space after the last number
                print("{:d}{:d}, ".format(i, j), end='')
            else:
                print("{:d}{:d}".format(i, j))
