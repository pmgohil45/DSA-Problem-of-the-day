"""
Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.

Examples:

Input: LinkedList: 1 → 2 → 1 → 1 → 2 → 1
Output: true
Explanation: The given linked list is 1 → 2 → 1 → 1 → 2 → 1 , which is a palindrome and Hence, the output is true.
1 → 2 → 1
        ↓
        1 → 2 → 1

Input: LinkedList: 1 → 2 → 3 → 4
Output: false
Explanation: The given linked list is 1->2->3->4, which is not a palindrome and Hence, the output is false.
1 → 2 → 3 → 4

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1) 
Note: You should not use the recursive stack space as well

Constraints:
1 <= number of nodes <= 10^5
1 ≤ node->data ≤ 10^3
"""
"""
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
"""
#Function to check whether the list is palindrome.
class Solution:
    # Function to check whether the list is palindrome.
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list using slow and fast pointers.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list starting from slow.
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Compare the first half and the reversed second half.
        first_half, second_half = head, prev
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        # If all nodes matched, it's a palindrome.
        return True
