/*
Given an array arr[] and two integers say, x and y, find the number of sub-arrays in which the number of occurrences of x is equal to the number of occurrences of y.

Examples:

Input: arr[] = [1, 2, 1] , x= 1 , y = 2
Output: 2
Explanation: The possible sub-arrays have same equal number of occurrences of x and y are:
1) [1, 2], x and y have same occurrence(1).
2) [2, 1], x and y have same occurrence(1).

Input: arr[] = [1, 2, 1] , x = 4 , y = 6
Output: 6
Explanation: The possible sub-arrays have same equal number of occurrences of x and y are:
1) [1], x and y have same occurrence(0).
2) [2], x and y have same occurrence(0).
3) [1], x and y have same occurrence(0).
4) [1, 2], x and y have same occurrence(0).
5) [2, 1], x and y have same occurrence(0).
6) [1, 2, 1], x and y have same occurrence(0).

Input: arr[] = [1, 2, 1] , x= 1 , y = 4
Output: 1
Explanation: The possible sub-array have same equal number of occurrences of x and y is: [2], x and y have same occurrence(0)

Constraints: 
1 <= arr.size() <= 10^6
1 <= arr[i], x, y<=10^6
*/
class Solution {
  public:
    int sameOccurrence(vector<int>& arr, int x, int y) {
        int n = arr.size(); // Get the size of the array
        // Arrays to store count of x and y up to each index
        vector<int> countX(n), countY(n);
        map<int, int> m; // To store counts of same diffs

        // Count occurrences of x and y
        for (int i = 0; i < n; i++) {
            if (arr[i] == x) {
                countX[i] = (i != 0) ? countX[i - 1] + 1 : 1;
            } else {
                countX[i] = (i != 0) ? countX[i - 1] : 0;
            }

            if (arr[i] == y) {
                countY[i] = (i != 0) ? countY[i - 1] + 1 : 1;
            } else {
                countY[i] = (i != 0) ? countY[i - 1] : 0;
            }

            // Increment count of current difference (countX - countY)
            m[countX[i] - countY[i]]++;
        }

        // Traverse map and compute the result
        int result = m[0]; // Number of subarrays where countX == countY
        for (auto it = m.begin(); it != m.end(); ++it) {
            long long freq = it->second;
            // Combination formula for counting pairs
            result = result + (freq * (freq - 1)) / 2LL;
        }

        return result;
    }
};
