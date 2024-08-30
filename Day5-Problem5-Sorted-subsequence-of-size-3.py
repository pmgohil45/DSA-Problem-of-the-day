"""
You are given an array arr, you need to find any three elements in it such that arr[i] < arr[j] < arr[k] and i < j < k.

Note:

The output will be 1 if the subsequence returned by the function is present in the array arr
If the subsequence is not present in the array then return an empty array, the driver code will print 0.
If the subsequence returned by the function is not in the format as mentioned then the output will be -1.

Examples :

Input: arr = [1, 2, 1, 1, 3]
Output: 1
Explanation: A subsequence 1 2 3 exist.

Input: arr = [1, 1, 3]
Output: 0
Explanation: No such Subsequence exist, so empty array is returned (the driver code automatically prints 0 in this case).

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 106

"""
class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        
        if n < 3:
            return []
        
        # Arrays to store the left minimum and right maximum elements.
        left_min = [0] * n
        right_max = [0] * n
        
        # Fill left_min[]
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])
        
        # Fill right_max[]
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        
        # Traverse array to find the valid subsequence
        for j in range(1, n - 1):
            if arr[j] > left_min[j - 1] and arr[j] < right_max[j + 1]:
                # Found the valid subsequence
                return [left_min[j - 1], arr[j], right_max[j + 1]]
        
        # If no such subsequence found, return an empty array
        return []
