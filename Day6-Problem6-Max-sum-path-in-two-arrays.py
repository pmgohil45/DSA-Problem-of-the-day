"""
Given two sorted arrays of distinct integers arr1 and arr2. Each array may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any array. You can switch from one array to another array only at the common elements.

Note:  When we switch from one array to other,  we need to consider the common element only once in the result.

Examples : 

Input: arr1 = [2, 3, 7, 10, 12] , arr2 = [1, 5, 7, 8]
Output: 35

Explanation: The path will be 1+5+7+10+12 = 35, where 1 and 5 come from arr2 and then 7 is common so we switch to arr1 and add 10 and 12.
Input: arr1 = [1, 2, 3] , arr2[] = [3, 4, 5]
Output: 15

Explanation: The path will be 1+2+3+4+5=15.
Expected Time Complexity: O(m + n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr1.size(), arr2.size() <= 104
1 <= arr1[i], arr2[i] <= 105
"""
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Initialize the indexes for arr1 and arr2
        i, j = 0, 0
        # Initialize the sums for the two paths
        sum1, sum2 = 0, 0
        # Initialize the result
        result = 0

        # Traverse both arrays until we reach the end of one of them
        while i < len(arr1) and j < len(arr2):
            # If arr1[i] is smaller, add it to sum1
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            # If arr2[j] is smaller, add it to sum2
            elif arr2[j] < arr1[i]:
                sum2 += arr2[j]
                j += 1
            else:
                # If arr1[i] == arr2[j], then it's a common element.
                # Add the maximum of the two sums to the result
                result += max(sum1, sum2) + arr1[i]
                # Reset the sums
                sum1, sum2 = 0, 0
                # Move to the next elements in both arrays
                i += 1
                j += 1

        # Add remaining elements of arr1 (if any)
        while i < len(arr1):
            sum1 += arr1[i]
            i += 1

        # Add remaining elements of arr2 (if any)
        while j < len(arr2):
            sum2 += arr2[j]
            j += 1

        # Add the maximum of the remaining sums to the result
        result += max(sum1, sum2)

        return result
