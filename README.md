# Here is my HackerRank Solutions

> The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

---
## Solution Approach

>You can find the problem statements and descriptions for these solutions by following the provided commands within the Python programs or by visiting the Hackerrank website [here](https://www.hackerrank.com/challenges). Simply search for the program name to access the detailed problem statement.

---
### Diagonal Difference

- [Solution](./python/DiagonalDifference.py)

### - Explanation:

        1. primary_diagonal_sum and secondary_diagonal_sum are initialized to 0 to store the sums of the primary and secondary diagonals, respectively.

        2. The function iterates through the rows of the matrix. For each row i, it adds the element at position (i, i) (primary diagonal) to primary_diagonal_sum and the element at position (i, len(arr) - 1 - i) (secondary diagonal) to secondary_diagonal_sum.

        3. After iterating through the matrix, the function calculates the absolute difference between primary_diagonal_sum and secondary_diagonal_sum.

        4. The absolute difference is returned as the result, representing the diagonal difference of the input matrix.

---

### Extra Long Factorials

- [Solution](./python/ExtraLongFactorials.py)

### - Explanation:

        1. result = 1: Initialize the result variable as 1 to store the factorial value.

        2. Use a for loop to iterate through the numbers from 1 to n (inclusive). For each iteration, multiply the current result value by the loop variable i.

        3. After the loop completes, result contains the factorial of the input number n.

        4. Print the calculated factorial using the print function.
---

### The Full Counting Sort

- [Solution](./python/The%20FullCountingSort.py)

### - Explanation:

        1. Create an empty list called sorted_list to store strings based on their index positions. The list has 100 empty sublists, assuming indices are between 0 and 99.

        2. Iterate through the input list arr. For each element, extract the index value and the string value.

        3. If the current element is in the first half of the input list, replace the string with "-" (according to the problem's specification).

        4. Place the string in the appropriate index position in the sorted_list.

        5. After processing all elements, concatenate the strings in each index position to form the final sorted result.

        6. Print the sorted result as a space-separated string.
---

### Apple and Orange

- [Solution](./python/AppleandOrange.py)

### - Explanation:

        1. Initialize apple_count and orange_count variables to keep track of the number of apples and oranges within the range [s, t].

        2. Calculate the actual landing positions of apples and oranges by adding their distances (apples and oranges arrays) to the respective trees (a and b).

        3. Iterate through the apple positions and count how many fall within the specified range [s, t]. Increment apple_count for each apple that falls within the range.

        4. Iterate through the orange positions and count how many fall within the specified range [s, t]. Increment orange_count for each orange that falls within the range.

        5. Print the counts of apples and oranges that fall within the specified range.


---

### Between Two Sets

- [Solution](./python/BetweenTwoSets.py)

### - Explanation:

        1. Find the maximum element in array a and the minimum element in array b as max_a and min_b.

        2. Iterate through all integers from max_a to min_b (inclusive).

        3. For each number, check if it is divisible by all elements in array a using a generator expression and the all() function.

        4. If the number is divisible by all elements in array a, check if all elements in array b are divisible by the current number using another generator expression and the all() function.

        5. If both conditions are met, increment the count variable.

        6.After iterating through all integers, return the count as the result, representing the number of integers satisfying the conditions.

---

### Grading Students

- [Solution](./python/GradingStudents.py)

### - Explanation:

        1. Create an empty list called rounded_grades to store the rounded grades.

        2. Iterate through the input grades. For each grade, check if it's less than 38. If it is, add the grade to rounded_grades without rounding.

        3. If the grade is 38 or higher, calculate the next multiple of 5 greater than or equal to the grade.

        4. Check if the difference between the next multiple and the grade is less than 3. If it is, round up the grade by using the next multiple of 5. Otherwise, keep the grade unchanged.

        5. After iterating through all grades, return the rounded_grades list, which contains the rounded grades based on the specified rules.

---

### Electronics Shop

- [Solution](./python/ElectronicsShop.py)

### - Explanation:

        1. Initialize max_spent as -1, indicating that it's not possible to purchase both items within the budget.

        2. Iterate through all combinations of keyboards and drives using nested loops.

        3. For each combination, calculate the total cost (total_cost) by adding the cost of the current keyboard and drive.

        4. Check if the total_cost is within budget (total_cost <= b) and if it's greater than the current max_spent. If both conditions are met, update max_spent with the total_cost.

        5. After iterating through all combinations, max_spent contains the maximum amount that can be spent on a keyboard and a USB drive within the budget. If no valid combination is found, max_spent remains -1.

        6. Return the max_spent value as the result, indicating the maximum amount that can be spent on both items within the budget or -1 if it's not possible.


---

### Viral Advertising

- [Solution](./python/ViralAdvertising.py)

### - Explanation:

        1. total_likes is initialized to 0 to store the cumulative likes received over n days.

        2. shared is initialized to 5 representing the initial number of people the advertisement is shared with on the first day.

        3. Iterate through the number of days using the variable day.

        4. For each day, calculate the number of likes received (likes) by dividing the current shared count by 2. Add this to the total_likes.

        5. Update the shared count for the next day by multiplying the current likes by 3.

        6. After iterating through all days, total_likes contains the total number of likes received over n days.

        7. Return the total_likes as the result, indicating the cumulative number of people who liked the advertisement.


---

### Minimum Distances

- [Solution](./python/MinimumDistances.py)

### - Explanation:

        1. Create a dictionary element_indices to store the most recent index of each element encountered in the array a.

        2. Initialize the min_distance variable to a large value (float('inf')).

        3. Iterate through the array a using enumeration to keep track of the indices.

        4. For each element, check if it has been encountered before (num in element_indices). If it has, calculate the distance between the current index and the most recent index where the element was seen (i - element_indices[num]). Update min_distance with the smaller value between the current minimum distance and the calculated distance.

        5. Update the most recent index of the current element in the element_indices dictionary.

        6. After iterating through the array, if min_distance remains as the initial large value, it means no equal elements were found, so return -1. Otherwise, return the calculated min_distance representing the minimum distance between equal elements.

---

### Service Lane

- [Solution](./python/ServiceLane.py)

### - Explanation:

        1. Initialize an empty list called min_width_vehicles to store the minimum width vehicles for each test case.

        2. Iterate through the test cases in the cases list.

        3. For each test case, extract the starting index (start_index) and ending index (end_index) of the segment from the current case.

        4. Use list slicing (width[start_index:end_index + 1]) to get the segment from the width list and find the minimum value in the segment using the min() function. This represents the minimum width vehicle that can pass through the current segment.

        5. Add the minimum width value to the min_width_vehicles list.

        6. After processing all test cases, return the min_width_vehicles list, which contains the minimum width vehicles that can pass through each segment of the service lane.
---
