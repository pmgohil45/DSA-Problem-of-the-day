/*
Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.

Examples:

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.

Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= arr.size() <= 10^6
1 <= arr[i] <= 10^9
*/
// User function Template for javascript

/**
 * @param {number[]} arr
 * @return {number}
 */

class Solution {
    maxDistance(arr) {
        let n = arr.length;
        let mp = new Map();
        let max_dist = 0;
        for (let i = 0; i < n; i++) {
            if (!mp.has(arr[i])) {
                mp.set(arr[i], i);
            } else {
                max_dist = Math.max(max_dist, i - mp.get(arr[i]));
            }
        }
        return max_dist;
    }
}
