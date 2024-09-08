/*
Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 
Explanation:First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 

Input: arr = {1, 4, 3, 2, 6, 7}
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.

Input: arr = {0, 10, 20}
Output: -1
Explanation: We cannot go anywhere from the 1st element.

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
0 ≤ arr[i] ≤ 105
2 ≤ arr.size() ≤ 106
*/

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        
        // Edge case: If there's only one element, no jump is needed.
        if (n == 1) return 0;
        
        // Edge case: If the first element is 0, we can't make any jump.
        if (arr[0] == 0) return -1;
        
        int jumps = 0;     // Counts the minimum jumps required
        int farthest = 0;  // Tracks the farthest index we can reach
        int current_end = 0; // The end of the range for the current jump
        
        // Traverse the array
        for (int i = 0; i < n - 1; ++i) {
            // Update the farthest index that can be reached
            farthest = max(farthest, i + arr[i]);
            
            // If we have reached the end of the current jump range
            if (i == current_end) {
                jumps++;
                current_end = farthest; // Move the current end to the farthest we can reach
                
                // If the current end reaches or exceeds the last index, we are done
                if (current_end >= n - 1) return jumps;
            }
            
            // If the farthest we can reach doesn't move beyond i, we can't reach the end
            if (farthest <= i) return -1;
        }
        
        // If we exit the loop without having reached the last index
        return -1;
    }
};
