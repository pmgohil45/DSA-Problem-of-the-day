"""
Given an array height representing the heights of buildings. You have to count the buildings that will see the sunrise (Assume the sun rises on the side of the array starting point).
Note: The height of the building should be strictly greater than the height of the buildings left in order to see the sun.

                                                          ____
                                                         |    |
     O O O O O                                           |    |
   O           O                            ____         |    |
  O     SUN     O                          |    |        |    |
   O           O              ____         |    |        |    |
     O O O O O               |    |        |    |  ____  |    |
                             |    |        |    | |    | |    |
                             |    |        |    | |    | |    |
                             |    |        |    | |    | |    |
                             |    |  ____  |    | |    | |    |
                             |    | |    | |    | |    | |    |
                             |    | |    | |    | |    | |    |
                             |    | |    | |    | |    | |    | 
  ___________________________|____|_|____|_|____|_|____|_|____|_
  ←----------------Buildings of different hights---------------→

Examples :

Input: height = [7, 4, 8, 2, 9]
Output: 3
Explanation: As 7 is the first element, it can see the sunrise. 4 can't see the sunrise as 7 is hiding it. 8 can see. 2 can't see the sunrise. 9 also can see the sunrise.

Input: height = [2, 3, 4, 5]
Output: 4
Explanation: As 2 is the first element, it can see the sunrise.  3 can see the sunrise as 2 is not hiding it. Same for 4 and 5, they also can see the sunrise.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ height.size() ≤ 10^6
1 ≤ heighti ≤ 10^8
"""

class Solution:
    # Returns count of buildings that can see the sunrise
    def countBuildings(self, height):
        count = 1  # The first building always sees the sunrise
        max_height = height[0]  # Initialize with the first building's height

        # Iterate through the buildings starting from the second one
        for i in range(1, len(height)):
            if height[i] > max_height:
                count += 1  # This building can see the sunrise
                max_height = height[i]  # Update the max height

        return count

# Example usage
sol = Solution()

# Test case 1
#height1 = [7, 4, 8, 2, 9]
#print(sol.countBuildings(height1))  # Output: 3

# Test case 2
#height2 = [2, 3, 4, 5]
#print(sol.countBuildings(height2))  # Output: 4
