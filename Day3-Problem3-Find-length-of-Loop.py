"""
Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
1 → 2 → 3 → |
    ↑       ↓
    5 ← 4 ← |

Note: 'c' is the position of the node which is the next pointer of the last node of the linkedlist. If c is 0, then there is no loop.

Examples:

Input: LinkedList: 25->14->19->33->10->21->39->90->58->45, c = 4
Output: 7
Explanation: The loop is from 33 to 45. So length of loop is 33->10->21->39-> 90->58->45 = 7. 
The number 33 is connected to the last node of the linkedlist to form the loop because according to the input the 4th node from the beginning(1 based indexing) 
will be connected to the last node for the loop.
25 → 14 → 19 → 33 → 10 → 21 → 39 → |
                \                  ↓
                 |← 45 ← 58 ← 90 ← |
 
Input: LinkedList: 5->4, c = 0
Output: 0
Explanation: There is no loop.
5 → 4

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= no. of nodes <= 106
0 <= node.data <=106
0 <= c<= n-1
"""
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head
        
        # Step 1: Detect Loop
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next     # Move fast pointer two steps
            
            # Loop detected
            if slow == fast:
                return self.countLoopLength(slow)
        
        # No loop present
        return 0
    
    # Function to count the number of nodes in the loop
    def countLoopLength(self, node_in_loop):
        count = 1
        current = node_in_loop
        
        # Traverse the loop until we come back to the same node
        while current.next != node_in_loop:
            count += 1
            current = current.next
        
        return count
