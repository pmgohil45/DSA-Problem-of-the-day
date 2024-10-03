/*
You are given an array of integer nums[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return -1. 

Examples:

Input: nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: nums = [1, 2, 3, 4, 5]
Output: [-1]
Explanation: no candidate occur more than n/3 times.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraint:
1 <=  nums.size()  <= 10^6
-109 <= nums[i] <= 10^9
*/
class Solution {
    // Function to find the majority elements in the array
    findMajority(nums) {
        let n = nums.length;
        let num1 = 0, num2 = 0, c1 = 0, c2 = 0;
        let res = [];

        // Finding the two most frequent numbers using Boyer-Moore algorithm
        for (let x of nums) {
            if (x === num1) {
                c1++;
            } else if (x === num2) {
                c2++;
            } else if (c1 === 0) {
                num1 = x;
                c1 = 1;
            } else if (c2 === 0) {
                num2 = x;
                c2 = 1;
            } else {
                c1--;
                c2--;
            }
        }

        c1 = 0;
        c2 = 0;
        // Counting the occurrences of num1 and num2
        for (let x of nums) {
            if (x === num1) {
                c1++;
            } else if (x === num2) {
                c2++;
            }
        }

        // Checking if num1 and num2 are majority elements
        if (c1 > Math.floor(n / 3)) res.push(num1);
        if (c2 > Math.floor(n / 3)) res.push(num2);

        // If no majority elements, add -1 to the result list
        if (res.length === 0) res.push(-1);
        return res;
    }
}
