"""
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum

Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.

Expected Time Complexity: O(n*k)
Expected Auxilary Space: O(n)

Constraint:
1<= arr.size() <=10^4
1 <= k <= 100
1 <= arr[i] <= 10^4
"""
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(1, k+1):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j] + abs(arr[i] - arr[i-j]))
        
        return dp[-1]
