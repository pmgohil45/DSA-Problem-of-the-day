"""
Given an array arr integers. Do the following operation until a single element left. For every k^th operation:

Right, rotate the vector clockwise by 1.
Delete the k^th element from the last.
Now, find the element which is left at last.

Example:

Input: arr = [1, 2, 3, 4, 5, 6]
Output: 3
Explanation: Rotate the vector clockwise i.e. after rotation the vector arr = [6, 1, 2, 3, 4, 5] and delete the last element that is 5 that will be arr = [6, 1, 2, 3, 4]. Similarly, the output will be 3.

Input: arr = [1, 2, 3, 4]
Output: 2
Explanation: Rotate the vector clockwise i.e. after rotation the vector arr = [4, 1, 2, 3] and delete the last element that is 3 that will be arr = [4, 1, 2]. Similarly, the output will be 2.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 10^5
1 <= arr[i] <= 10^6
"""
class Solution:

    def rotateDelete(self, arr):
        i = 1
        n = len(arr)
        while i < (n / 2) + 1:
            arr.insert(0, arr.pop())  # Rotate the array
            arr.pop(-i)  # Delete the element
            i += 1

        return arr[0]
