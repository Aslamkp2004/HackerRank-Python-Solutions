#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0
    
    
    apple_positions = [a + d for d in apples]
    orange_positions = [b + d for d in oranges]
    
    for position in apple_positions:
        if s <= position <= t:
            apple_count += 1
    
    for position in orange_positions:
        if s <= position <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

#Explanation:
"""
1. Initialize apple_count and orange_count variables to keep track of the number of apples and oranges within the range [s, t].

2. Calculate the actual landing positions of apples and oranges by adding their distances (apples and oranges arrays) to the respective trees (a and b).

3. Iterate through the apple positions and count how many fall within the specified range [s, t]. Increment apple_count for each apple that falls within the range.

4. Iterate through the orange positions and count how many fall within the specified range [s, t]. Increment orange_count for each orange that falls within the range.

5. Print the counts of apples and oranges that fall within the specified range.

This logic ensures that the function accurately counts the apples and oranges that land within the given range along the straight line.
"""
