"""
Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.

Note: The output could be large take modulo 10^9+7.

Examples :

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation: 
3 → 2
X   2
------
6 → 4
Multiplication of 32 and 2 gives 64.

Input: LinkedList L1: 1->0->0 , LinkedList L2 : 1->0
Output: 1000
Explanation: 
    1 → 0 → 0
    X   1 → 0
---------------
1 → 0 → 0 → 0
Multiplication of 100 and 10 gives 1000.

Expected Time Complexity: O(max(n,m))
Expected Auxilliary Space: O(1)
where n is the size of L1 and m is the size of L2

Constraints:
1 <= number of nodes <= 10^5
1 <= node->data <= 10^3
"""
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    MOD = 10**9 + 7

    # Helper function to convert linked list to number
    def listToNumber(self, head):
        num = 0
        while head:
            num = (num * 10 + head.data) % self.MOD
            head = head.next
        return num
    
    # Function to multiply two linked lists.
    def multiply_two_lists(self, first, second):
        # Convert both linked lists to numbers
        num1 = self.listToNumber(first)
        num2 = self.listToNumber(second)
        
        # Multiply the two numbers and take the result mod MOD
        result = (num1 * num2) % self.MOD
        
        return result
