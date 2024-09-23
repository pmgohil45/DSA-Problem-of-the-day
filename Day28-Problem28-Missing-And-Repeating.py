"""
Given an unsorted array arr of of positive integers. One number 'A' from set {1, 2,....,n} is missing and one number 'B' occurs twice in array. Find numbers A and B.

Examples

Input: arr[] = [2, 2]
Output: 2 1
Explanation: Repeating number is 2 and smallest positive missing number is 1.

Input: arr[] = [1, 3, 3] 
Output: 3 2
Explanation: Repeating number is 3 and smallest positive missing number is 2.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ n ≤ 10^5
1 ≤ arr[i] ≤ n
"""
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        missing = -1
        repeating = -1

        # Mark elements visited by negating the value at the index corresponding to the value in the array
        for i in range(n):
            val = abs(arr[i]) - 1  # 1-based index to 0-based
            if arr[val] < 0:
                repeating = abs(arr[i])  # If already visited, it is the repeating number
            else:
                arr[val] = -arr[val]  # Mark as visited

        # Find the missing number
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1  # The index + 1 where the value is positive is the missing number

        return repeating, missing
