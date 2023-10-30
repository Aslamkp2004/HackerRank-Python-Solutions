#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    # Write your code here
    min_width_vehicles = []
    
    # Iterate through the test cases.
    for case in cases:
        # Extract the starting and ending indices of the segment from the test case.
        start_index, end_index = case[0], case[1]
        
        # Find the minimum width vehicle that can pass through the current segment.
        min_width = min(width[start_index:end_index + 1])
        
        # Add the minimum width to the result list.
        min_width_vehicles.append(min_width)
    
    return min_width_vehicles
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
