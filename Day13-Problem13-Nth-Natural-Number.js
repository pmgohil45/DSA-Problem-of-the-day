/*
Given a positive integer n. You have to find nth natural number after removing all the numbers containing the digit 9.

Examples :

Input: n = 8
Output: 8
Explanation: After removing natural numbers which contains digit 9, first 8 numbers are 1,2,3,4,5,6,7,8 and 8th number is 8.

Input: n = 9
Output: 10
Explanation: After removing natural numbers which contains digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10 and 9th number is 10.

Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 109

*/
/**
 * @param {number} n
 * @returns {number}
 */

class Solution {
    findNth(n) {
        let result = 0;
        let multiplier = 1;
        
        // Convert n to base-9 equivalent
        while (n > 0) {
            result += (n % 9) * multiplier;
            n = Math.floor(n / 9);
            multiplier *= 10;
        }
        
        return result;
    }
}

