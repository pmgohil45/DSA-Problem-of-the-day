"""
Given an integer array arr of integers, the task is to find the maximum absolute difference between the nearest left smaller element and the nearest right smaller element of every element in array arr. If for any component of the arr, the nearest smaller element doesn't exist then consider it as 0.

Examples :

Input: arr = [2, 1, 8]
Output: 1
Explanation: left smaller array ls = [0, 0, 1], right smaller array rs = [1, 0, 0]. Maximum Diff of abs(ls[i] - rs[i]) = 1
Input: arr = [2, 4, 8, 7, 7, 9, 3]
Output: 4
Explanation: left smaller array ls = [0, 2, 4, 4, 4, 7, 2], right smaller rs = [0, 3, 7, 3, 3, 3, 0]. Maximum Diff of abs(ls[i] - rs[i]) = abs(7 - 3) = 4
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1 <= arr.size() <= 10^6
1<= arr[i] <=10^9
"""

class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        
        # Arrays to store nearest smaller elements to left and right
        nsl = [0] * n  # Nearest smaller to left
        nsr = [0] * n  # Nearest smaller to right
        
        # Stack to help in finding nearest smaller to left
        stack = []
        
        # Finding nearest smaller to left
        for i in range(n):
            # Pop elements from stack that are greater or equal to arr[i]
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            # If stack is not empty, top of the stack is the NSL
            if stack:
                nsl[i] = stack[-1]
            else:
                nsl[i] = 0  # If no smaller element to the left, set it to 0
            # Push current element to stack
            stack.append(arr[i])
        
        # Clear the stack for next computation
        stack.clear()
        
        # Finding nearest smaller to right
        for i in range(n-1, -1, -1):
            # Pop elements from stack that are greater or equal to arr[i]
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            # If stack is not empty, top of the stack is the NSR
            if stack:
                nsr[i] = stack[-1]
            else:
                nsr[i] = 0  # If no smaller element to the right, set it to 0
            # Push current element to stack
            stack.append(arr[i])
        
        # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(nsl[i] - nsr[i]))
        
        return max_diff

