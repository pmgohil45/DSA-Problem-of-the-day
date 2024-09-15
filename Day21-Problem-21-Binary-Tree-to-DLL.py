"""
Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes will be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as the order of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.

          10
      /         \
     12          15
  /      \      /
 25      30    36

The above tree should be in place converted to following Doubly Linked List(DLL).
head
   \
   25 ←→ 12 ←→ 30 ←→ 10 ←→ 36 ←→ 15

Examples:
Input:
      1
    /   \
   3     2
Output:
3 1 2 
2 1 3
Explanation: DLL would be 3 ←→ 1 ←→ 2

Input:
        10
      /    \
     20    30
   /    \
  40    60
Output:
40 20 60 10 30 
30 10 60 20 40
Explanation:  DLL would be 40 ←→ 20 ←→ 60 ←→ 10 ←→ 30

Expected Time Complexity: O(no. of nodes)
Expected Space Complexity: O(height of the tree)

Constraints:
1 ≤ Number of nodes ≤ 10^5
0 ≤ Data of a node ≤ 10^5
"""
class Node:
    """ Class Node representing a tree node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None  # To store the previously visited node in inorder traversal
        self.head = None  # To store the head of the doubly linked list
    
    # Function to convert a binary tree to doubly linked list.
    def bToDLL(self, root):
        if root is None:
            return None
        
        # Convert the left subtree
        self.bToDLL(root.left)
        
        # Now process the current node
        if self.prev is None:
            # If this is the first node, make it head of the DLL
            self.head = root
        else:
            # Link the previous node (self.prev) and current node (root)
            root.left = self.prev
            self.prev.right = root
        
        # Move prev to current node
        self.prev = root
        
        # Convert the right subtree
        self.bToDLL(root.right)
        
        # Return the head of the DLL
        return self.head

# Helper function to print the Doubly Linked List from left to right
def print_dll_from_head(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.right
    print()

# Helper function to print the Doubly Linked List from right to left (for verification)
def print_dll_from_tail(tail):
    current = tail
    while current:
        print(current.data, end=" ")
        current = current.left
    print()

# Example usage:
if __name__ == "__main__":
    # Constructing the binary tree
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    sol = Solution()
    head = sol.bToDLL(root)
    
    # Print the Doubly Linked List from head to tail
    #print("DLL from head to tail:")
    #print_dll_from_head(head)

    # To print DLL from tail to head for verification
    # Find the tail first
    tail = head
    while tail and tail.right:
        tail = tail.right
    
    #print("DLL from tail to head:")
    #print_dll_from_tail(tail)
