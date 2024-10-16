"""
Given a permutation of some of the first natural numbers in an array arr[], determine if the array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

Return true if it is possible to sort the array with exactly two swaps, otherwise return false.

Examples:

Input: arr = [4, 3, 2, 1]
Output: true
Explanation: First, swap arr[0] and arr[3]. The array becomes [1, 3, 2, 4]. Then, swap arr[1] and arr[2]. The array becomes [1, 2, 3, 4], which is sorted.

Input: arr = [4, 3, 1, 2]
Output: false
Explanation: It is not possible to sort the array with exactly two swaps.

Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ arr.size()
"""
 class Solution:

    def doOneSwap(self, n, arr):
        for i in range(n):
            if arr[i] != i + 1:
                for j in range(i + 1, n):
                    if arr[j] == i + 1:
                        arr[i], arr[j] = arr[j], arr[i]
                        return

    def checkSorted(self, arr):
        n = len(arr)
        misMatch = 0

        # Count the number of mismatches
        for i in range(n):
            if arr[i] != i + 1:
                misMatch += 1

        # Handle edge cases based on mismatch count
        if n == 1:
            return False
        if misMatch == 0 or misMatch == 3:
            return True
        if misMatch != 4:
            return False

        # Try to sort the array with two swaps
        self.doOneSwap(n, arr)
        self.doOneSwap(n, arr)

        # Check if the array is now sorted
        for i in range(n):
            if arr[i] != i + 1:
                return False

        return True
