"""
Given an unsorted array arr containing both positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0 (zero) should be considered a positive element.

Examples:

Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: 9 -2 4 -1 5 -5 0 -3 2
Explanation: Positive elements : [9,4,5,0,2]
Negative elements : [-2,-1,-5,-3]
As we need to maintain the relative order of postive elements and negative elements we will pick each element from the positive and negative and will store them. If any of the positive and negative numbersare completed. we will continue with the remaining signed elements.
The output is 9,-2,4,-1,5,-5,0,-3,2.

Input: arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
Output: 5 -5 2 -2 4 -8 7 1 8 0
Explanation : Positive elements : [5,2,4,7,1,8,0]
Negative elements : [-5,-2,-8]
The output is 5, -5, 2, -2, 4, -8, 7, 1, 8, 0.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ arr.size() ≤ 10^7
-106 ≤ arr[i] ≤ 10^7
"""

class Solution:
    def rearrange(self, arr):
        # Separate positive and negative numbers
        positive = [x for x in arr if x >= 0]  # Considering 0 as a positive element
        negative = [x for x in arr if x < 0]
        
        result = []
        i, j = 0, 0  # Two pointers for positive and negative lists
        
        # We will interleave the positives and negatives
        while i < len(positive) and j < len(negative):
            result.append(positive[i])
            result.append(negative[j])
            i += 1
            j += 1
        
        # If there are remaining positive elements
        while i < len(positive):
            result.append(positive[i])
            i += 1
        
        # If there are remaining negative elements
        while j < len(negative):
            result.append(negative[j])
            j += 1
        
        # Copy the result back to the original array
        for idx in range(len(arr)):
            arr[idx] = result[idx]

# Example usage:
if __name__ == "__main__":
    arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
    sol = Solution()
    sol.rearrange(arr)
    #print(arr)  # Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
