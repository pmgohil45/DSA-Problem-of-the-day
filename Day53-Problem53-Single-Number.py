"""
Given an array arr[] of positive integers where every element appears even times except for one. Find that number occurring an odd number of times.

Examples:

Input: arr[] = [1, 1, 2, 2, 2]
Output: 2
Explanation: In the given array all element appear two times except 2 which appears thrice.

Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
Output: 1
Explanation: In the given array all element appear two times except 1 which appears once.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 10^6
0 ≤ arri ≤ 10^5
"""
class Solution:
    # Function to find the element in the array which occurs only once.
    def getSingle(self, arr):
        # Variable to store the XOR of all elements in the array.
        xr = 0

        # Iterating over all the elements in the array.
        for num in arr:
            # Calculating XOR of each element with the previous XOR.
            xr ^= num

        # Returning the element which occurs only once.
        return xr
