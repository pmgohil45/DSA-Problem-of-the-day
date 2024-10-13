"""
Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes present in even positions.

Examples :

Input: LinkedList: 1 → 2 → 3 → 4 → 5 → 6
Output: 1 → 3 → 5
Explanation: Deleting alternate nodes ie 2, 4, 6 results in the linked list with elements 1->3->5.

Input: LinkedList: 99 → 59 → 42 → 20
Output: 99 → 42

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= number of nodes <= 10^5
1 <= node->data <= 10^3
"""
'''
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None
'''

# Linked List class
class Solution:

    def deleteAlt(self, head):
        if not head:
            return

        prev = head
        node = head.next

        while prev and node:
            prev.next = node.next
            node = prev.next
            if node:
                prev = node
                node = node.next
