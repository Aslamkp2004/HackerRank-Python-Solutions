#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    result = 1
    
    # Calculate the factorial by multiplying numbers from 1 to n.
    for i in range(1, n + 1):
        result *= i
    
    # Print the calculated factorial.
    print(result)
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
