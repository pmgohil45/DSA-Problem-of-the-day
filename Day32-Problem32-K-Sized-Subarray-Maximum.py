"""
Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.

Examples:

Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6]
Output: [3, 3, 4, 5, 5, 5, 6] 
Explanation: 
1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6

Input: k = 4, arr[] = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
Output: [10, 10, 10, 15, 15, 90, 90]
Explanation: 
1st contiguous subarray = [8 5 10 7], max = 10
2nd contiguous subarray = [5 10 7 9], max = 10
3rd contiguous subarray = [10 7 9 4], max = 10
4th contiguous subarray = [7 9 4 15], max = 15
5th contiguous subarray = [9 4 15 12], max = 15
6th contiguous subarray = [4 15 12 90], max = 90
7th contiguous subarray = {15 12 90 13}, max = 90

Expected Time Complexity: O(n)-
Expected Auxiliary Space: O(k)

Constraints:
1 ≤ sizeof(arr) ≤ 10^6
1 ≤ k ≤ sizeof(arr)
0 ≤ arr[i] ≤ 10^9
"""

from collections import deque

class Solution:
    
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, k, arr):
        n = len(arr)
        if n == 0 or k == 0:
            return []
        
        # Initialize deque and result list
        dq = deque()
        result = []
        
        for i in range(n):
            # Remove elements not within the window of size k
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the back if they are smaller than
            # the current element since they cannot be the maximum
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # Add the current element at the back of the deque
            dq.append(i)
            
            # The front of the deque contains the index of the maximum element
            # for the current window
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result
