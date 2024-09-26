"""
You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the next adjacent building. You need to find the maximum number of consecutive steps you can put forward such that you gain an increase in altitude with each step.

Examples:

Input: arr[] = [1, 2, 2, 3, 2]
Output: 1
Explanation: 1, 2, or 2, 3 are the only consecutive buildings with increasing heights thus maximum number of consecutive steps with an increase in gain in altitude would be 1 in both cases.

Input: arr[] = [1, 2, 3, 4]
Output: 3
Explanation: 1 to 2 to 3 to 4 is the jump of length 3 to have a maximum number of buildings with increasing heights, so maximum steps with increasing altitude becomes 3.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 10^6
1 <= arr[i] <= 10^5
"""
class Solution:
    
    # Function to find the maximum number of consecutive steps 
    # to gain an increase in altitude with each step.
    def maxStep(self, arr):
        # Initialize the maximum steps and current steps to 0
        max_steps = 0
        current_steps = 0
        
        # Iterate through the array from the second element to the end
        for i in range(1, len(arr)):
            # If the current building is taller than the previous one
            if arr[i] > arr[i - 1]:
                # Increment the current step count
                current_steps += 1
                # Update the maximum steps if the current steps exceed it
                max_steps = max(max_steps, current_steps)
            else:
                # Reset the current steps count if the sequence is broken
                current_steps = 0
        
        # Return the maximum number of steps
        return max_steps
