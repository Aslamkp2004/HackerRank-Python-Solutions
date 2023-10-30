#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    total_likes = 0
    shared = 5
    
    # Iterate through the number of days.
    for day in range(n):
        # Calculate likes for the current day, add to the total_likes, and update shared count for the next day.
        likes = shared // 2
        total_likes += likes
        shared = likes * 3
    
    return total_likes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
