"""
Given an array arr[] of integers, the task is to count the number of ways to split given array elements into two disjoint groups such that the XOR of elements of each group is equal.
Note: The answer could be very large so print it by doing modulo with 109 + 7. 

Examples:

Input : arr[] = [1, 2, 3]
Output : 3
Explanation: {(1),(2, 3)}, {(2),(1, 3)}, {(3),(1, 2)} are three ways with equal XOR value of two groups.

Input : arr[] = [5, 2, 3, 2]
Output : 0
Explanation: No way to split into  two groups whose XOR is equal.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1<=arr.size()<=10^6
1<=arr[i]<=10^6
"""
class Solution:
    # Function to calculate (x^y) % p using binary exponentiation
    def power(self, x, y, p):
        result = 1
        x = x % p  # Ensure x is within mod range

        while y > 0:
            # If y is odd, multiply x with the result
            if (y & 1) == 1:
                result = (result * x) % p
            # y = y // 2
            y = y >> 1
            # x = x^2 % p
            x = (x * x) % p
        return result

    # Function to count the number of ways to split array into two groups such that each group has equal XOR value
    def countgroup(self, arr):
        mod = 1000000007  # Define the mod value
        n = len(arr)  # Get the size of the input array
        xs = 0  # Initialize XOR sum

        # Compute the XOR of the entire array
        for i in range(n):
            xs ^= arr[i]

        # We can split only if the XOR of the entire array is 0
        if xs == 0:
            # If XOR of the whole array is 0, calculate 2^(n-1) - 1
            ans = self.power(2, n - 1, mod) - 1
            if ans < 0:
                ans += mod  # Ensure the answer is non-negative
            return ans

        return 0  # If XOR isn't 0, we cannot split the array
