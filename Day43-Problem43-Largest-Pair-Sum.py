"""
Find the largest pair sum in an array of distinct integers.

Examples :

Input: arr[] = [12, 34, 10, 6, 40]
Output: 74
Explanation: Sum of 34 and 40 is the largest, i.e, 34 + 40 = 74.

Input: arr[] = [10, 20, 30]
Output: 50
Explanation: 20 + 30 = 50.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ arr.size() ≤ 10^6
0 ≤ arr[i] ≤ 10^6
"""
from typing import List


class Solution:

    def pairsum(self, arr: List[int]) -> int:
        # code here
        # Initialize first and second
        # largest element
        n = len(arr)
        if arr[0] > arr[1]:
            first = arr[0]
            second = arr[1]

        else:
            first = arr[1]
            second = arr[0]

        # Traverse remaining array and
        # find first and second largest
        # elements in overall array
        for i in range(2, n):

            # If current element is greater
            # than first then update both
            # first and second
            if arr[i] > first:
                second = first
                first = arr[i]

            # If arr[i] is in between first
            # and second then update second
            elif arr[i] > second:
                second = arr[i]

        return (first + second)
