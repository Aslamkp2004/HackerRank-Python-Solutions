#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    sorted_list = [[] for _ in range(100)]  # Assuming indices are between 0 and 99.
    
    # Iterate through the input list and place strings in the appropriate index positions.
    for i in range(len(arr)):
        index = int(arr[i][0])  # Extract the index value from the input list.
        string = arr[i][1]      # Extract the string value from the input list.
        
        # If it's the first half of the input list, replace the string with "-".
        if i < len(arr) // 2:
            string = "-"
        
        # Add the string to the corresponding index position in the sorted list.
        sorted_list[index].append(string)
    
    # Concatenate the strings in the sorted list to form the final sorted result.
    sorted_result = []
    for strings in sorted_list:
        sorted_result.extend(strings)
    
    # Print the sorted result as a space-separated string.
    print(" ".join(sorted_result))
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
