/*
Given an unsorted array of integers arr[], and a target tar, determine the number of subarrays whose elements sum up to the target value.

Examples:

Input: arr[] = [10, 2, -2, -20, 10] , tar = -10
Output: 3
Explanation: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].

Input: arr[] = [1, 4, 20, 3, 10, 5] , tar = 33
Output: 1
Explanation: Subarray with sum 33 is: [20,3,10].

Expected Time Complexity: O(n)
Expected Auxilary Space: O(n)

Constraints:
1 <= arr.size() <= 10^6
-105 <= arr[i] <= 10^5
-105 <= tar <= 10^5
*/
/**
 * @param {number[]} arr
 * @param {number} tar
 * @returns {number}
 */
class Solution {
    // Function to count the number of subarrays which adds to the given sum.
    subArraySum(arr, tar) {

        // using map to store the sum which has appeared already.
        let mp = new Map();
        let n = arr.length;

        let curr_sum = 0;
        let count = 0;

        // iterating over the array elements.
        for (let i = 0; i < n; i++) {
            // storing prefix sum which is sum of elements till current element.
            curr_sum = curr_sum + arr[i];

            // checking if sum up to current element is equal to the given sum.
            if (curr_sum == tar) {
                count++;
            }

            // if map contains (curr_sum - sum) i.e. difference of current and
            // given sum, it means there is a subarray with sum of elements
            // equal to sum given.
            if (mp.has(curr_sum - tar))
                // adding number of times (curr_sum-sum) has
                // appeared in map to the counter.
                count += mp.get(curr_sum - tar);

            // storing the prefix sum in map.
            if (!mp.has(curr_sum))
                mp.set(curr_sum, 1);
            else
                mp.set(curr_sum, mp.get(curr_sum) + 1);
        }
        // returning the count of subarrays.
        return count;
    }
}
