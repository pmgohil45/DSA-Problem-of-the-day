"""
Given a doubly linked list, each node is at most k-indices away from its target position. The problem is to sort the given doubly linked list. The distance can be assumed in either of the directions (left and right).

Examples :

Input: Doubly Linked List : 3 ←→ 2 ←→ 1 ←→ 5 ←→ 6 ←→ 4 , k = 2
Output: 1 ←→ 2 ←→ 3 ←→ 4 ←→ 5 ←→ 6

Explanation: After sorting the given 2-sorted list is 1 ←→ 2 ←→ 3 ←→ 4 ←→ 5 ←→ 6.
Input: Doubly Linked List : 5 ←→ 6 ←→ 7 ←→ 3 ←→ 4 ←→ 4 , k = 3
Output: 3 ←→ 4 ←→ 4 ←→ 5 ←→ 6 ←→ 7
Explanation: After sorting the given 3-sorted list is 3 ←→ 4 ←→ 4 ←→ 5 ←→ 6 ←→ 7.

Expected Time Complexity: O(n*logk)
Expected Auxiliary Space: O(k)

Constraints:
1 <= number of nodes <= 10^5
1 <= k < number of nodes
1 <= node → data <= 10^9
"""

from heapq import heappush, heappop

class Compare:

    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data


class Solution:
    # Function to sort a k-sorted doubly linked list
    def sortAKSortedDLL(self, head, k):
        # If the list is empty
        if head is None:
            return head

        # Min-heap to sort the DLL nodes
        pq = []

        # Create a Min Heap of first (k+1) elements from the input doubly linked list
        newHead = None
        last = None
        for i in range(k + 1):
            if head is not None:
                heapq.heappush(pq, Compare(head))
                head = head.next

        # Process the heap and sort the linked list
        while pq:
            min_node = heapq.heappop(pq).node

            if newHead is None:
                newHead = min_node
                newHead.prev = None
                last = newHead
            else:
                last.next = min_node
                min_node.prev = last
                last = min_node

            # If there are more nodes left in the input list
            if head is not None:
                heapq.heappush(pq, Compare(head))
                head = head.next

        # Set the last node's next to None
        last.next = None

        return newHead
