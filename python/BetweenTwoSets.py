#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    count = 0
    
    # Find the maximum element in array a and the minimum element in array b.
    max_a = max(a)
    min_b = min(b)
    
    # Iterate through all integers from max_a to min_b.
    for num in range(max_a, min_b + 1):
        # Check if the current number is divisible by all elements in array a.
        if all(num % factor == 0 for factor in a):
            # Check if all elements in array b are divisible by the current number.
            if all(factor % num == 0 for factor in b):
                # If both conditions are met, increment the counter.
                count += 1
    
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
