"""
Given a Binary Tree, convert it into its mirror.
         1                      1
        / \                    / \
       3   2                  2   3
          / \                / \
         5   4              4   5

Examples:
Input:
     1
    / \
   2   3
Output: 3 1 2
Explanation: The tree is
  1    (mirror)   1
 / \    →→→→→→→  / \
2    3          3   2
The inorder of mirror is 3 1 2

Input:
      10
     /  \
    20   30
   /  \
  40  60
Output: 30 10 60 20 40
Explanation: The tree is
     10    (mirror)     10
    /  \    →→→→→→→    /  \
   20  30             30   20
  /  \                    /  \
 40  60                  60  40
The inroder traversal of mirror is 30 10 60 20 40.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 10^5
1 ≤ Data of a node ≤ 10^5

Input Format:
The tree in the input is given in the form of a string as described below. 
The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.
For example:
    1                         1
   / \                     /    \
  2   3                   2      3
     / \      <-->       / \    /   \
    4   6               N   N  4     6
     \                        / \   / \
      5                      N   5  N  N
      /                         / \
     7                         7   N
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively convert the left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)

    # Helper function to perform in-order traversal
    def inorderTraversal(self, root):
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)

# Function to build a tree from a level order input
def buildTree(data):
    if not data or data[0] == "N":
        return None
    
    from collections import deque
    
    # Create the root of the tree
    root = Node(int(data[0]))
    queue = deque([root])
    
    # Starting index for child nodes
    i = 1
    while queue and i < len(data):
        currNode = queue.popleft()
        
        # Left child
        if data[i] != "N":
            currNode.left = Node(int(data[i]))
            queue.append(currNode.left)
        i += 1
        
        # Right child
        if i < len(data) and data[i] != "N":
            currNode.right = Node(int(data[i]))
            queue.append(currNode.right)
        i += 1
    
    return root

# Example usage
if __name__ == "__main__":
    # Input string representing level order traversal of the tree
    input_data = "1 2 3 N N 4 6 N 5 N N 7 N"
    data_list = input_data.split()

    # Build the tree
    root = buildTree(data_list)
    
    # Create solution object
    sol = Solution()
    
    # Print inorder traversal before mirroring
    #print("Inorder before mirroring:", sol.inorderTraversal(root))
    
    # Mirror the binary tree
    sol.mirror(root)
    
    # Print inorder traversal after mirroring
    #print("Inorder after mirroring:", sol.inorderTraversal(root))
