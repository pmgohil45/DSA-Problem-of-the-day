"""
Given an unsorted array arr[] of size n. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 

Note: Consider the array as circular.

Examples :
Input: n = 5, d = 2 arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.

Input: n = 10, d = 3 arr[] = {2,4,6,8,10,12,14,16,18,20}
Output: 8 10 12 14 16 18 20 2 4 6
Explanation: 2 4 6 8 10 12 14 16 18 20 when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

Your Task:
You need not print or read anything. You need to complete the function rotateArr() which takes the array, d, and n as input parameters and rotates the array by d elements. The array must be modified in-place without using extra space.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106
1 <= d <= 106
0 <= arr[i] <= 105

"""
class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, A, D, N):
        # Ensure D is within bounds
        D = D % N

        # Helper function to reverse a part of the array
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the first D elements
        reverse(A, 0, D - 1)
        
        # Step 2: Reverse the remaining N-D elements
        reverse(A, D, N - 1)
        
        # Step 3: Reverse the entire array
        reverse(A, 0, N - 1)
