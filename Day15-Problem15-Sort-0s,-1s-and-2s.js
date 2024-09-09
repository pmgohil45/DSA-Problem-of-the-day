/*
Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[]= [0, 2, 1, 2, 0]
Output: 0 0 1 2 2
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 0]
Output: 0 0 1
Explanation: 0s 1s and 2s are segregated into ascending order.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 10^6
0 <= arr[i] <= 2
*/
class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    sort012(arr) {
        let low = 0, mid = 0, high = arr.length - 1;

        while (mid <= high) {
            if (arr[mid] === 0) {
                // Swap arr[mid] and arr[low]
                [arr[low], arr[mid]] = [arr[mid], arr[low]];
                low++;
                mid++;
            } else if (arr[mid] === 1) {
                mid++;
            } else {
                // Swap arr[mid] and arr[high]
                [arr[high], arr[mid]] = [arr[mid], arr[high]];
                high--;
            }
        }
    }
}
