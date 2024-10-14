"""
Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

Examples :

Input: LinkedList : 1 → 2 → 3 → 4 → 5

Output: 5
Explanation: Count of nodes in the linked list is 5, which is its length.
Input: LinkedList : 2 → 4 → 6 → 7 → 5 → 1 → 0
 
Output: 7
Explanation: Count of nodes in the linked list is 7. Hence, the output is 7.
Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
1 <= number of nodes <= 10^5
1 <= node->data <= 10^3
"""

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0

        # using a pointer for the linked list.
        current = head

        # using a loop to count nodes until we get null in link part of node.
        while current is not None:
            # updating counter.
            count += 1

            # updating pointer to the next node.
            current = current.next

        # returning the number of nodes.
        return count
