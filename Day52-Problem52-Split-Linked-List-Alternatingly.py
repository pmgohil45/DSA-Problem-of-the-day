"""
Given a singly linked list's head. Your task is to complete the function alternatingSplitList() that splits the given linked list into two smaller lists. The sublists should be made from alternating elements from the original list.
Note: 

The sublist should be in the order with respect to the original list.
Your have to return an array containing the both sub-linked lists.
Examples:

Input: LinkedList = 0 → 1 → 0 → 1 → 0 → 1
Output: 0 → 0 → 0 , 1 → 1 → 1
Explanation: After forming two sublists of the given list as required, we have two lists as: 0 → 0 → 0 and 1 → 1 → 1.

Input: LinkedList = 2 → 5 → 8 → 9 → 6
Output: 2 → 8 → 6 , 5 → 9
Explanation: After forming two sublists of the given list as required, we have two lists as: 2 → 8 → 6 and 5 → 9.

Input: LinkedList: 7 
Output: 7 , <empty linked list>

Constraints:
1 <= number of nodes <= 100
1 <= node → data <= 10^4
"""
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    # Function to append a new node with newData at the end of a linked list
    def append(self, headRef, newData):
        new_node = Node(newData)
        last = headRef[0]

        if headRef[0] is None:
            headRef[0] = new_node
            return

        while last.next:
            last = last.next
        last.next = new_node

    # Function to split a linked list into two lists alternately
    def alternatingSplitList(self, head):
        a = [None]
        b = [None]
        current = head

        while current:
            self.append(a, current.data)
            current = current.next

            if current:
                self.append(b, current.data)
                current = current.next

        return [a[0], b[0]]
