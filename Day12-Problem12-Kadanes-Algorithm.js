/*
Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.

Examples:

Input: arr[] = [1, 2, 3, -2, 5]
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

Input: arr[] = [-1, -2, -3, -4]
Output: -1
Explanation: Max subarray sum is -1 of element (-1)

Input: arr[] = [5, 4, 7]
Output: 16
Explanation: Max subarray sum is 16 of element (5, 4, 7)

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 105
-107 ≤ arr[i] ≤ 107
*/
/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution {
    // Function to find the sum of contiguous subarray with maximum sum.
    maxSubarraySum(arr) {
        // Initialize max_so_far and current_max to the first element of the array
        let max_so_far = arr[0];
        let current_max = arr[0];

        // Iterate through the array starting from the second element
        for (let i = 1; i < arr.length; i++) {
            // Update current_max to be the maximum of the current element
            // or the current element added to current_max
            current_max = Math.max(arr[i], current_max + arr[i]);
            
            // Update max_so_far to be the maximum of max_so_far and current_max
            max_so_far = Math.max(max_so_far, current_max);
        }

        // Return the maximum subarray sum found
        return max_so_far;
    }
}
