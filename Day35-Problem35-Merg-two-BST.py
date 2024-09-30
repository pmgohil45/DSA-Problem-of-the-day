"""
Given two BSTs, return elements of merged BSTs in sorted form.

Examples:

Input: 
BST1:
      5
     / \
    3   6
   / \
  2   4
BST2:
     2
    / \
   1   3
        \
         7
        /
       6
Output: 1 2 2 3 3 4 5 6 6 7
Explanation: After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.

Input: 

BST1:
      12
     / 
    9
   / \
  6   11
BST2:
     8
    / \
   5   10
  /
 6
Output: 2 5 6 8 9 10 11 12
Explanation: After merging and sorting the two BST we get 2 5 6 8 9 10 11 12.

Expected Time Complexity: O((m+n)*log(m+n))
Expected Auxiliary Space: O(Height of BST1 + Height of BST2 + m + n)

Constraints:
1 ≤ Number of Nodes, value of nodes ≤ 10^5
"""
class Solution:
    
    # Helper function to perform inorder traversal of a BST.
    def inorder(self, root, result):
        if root is None:
            return
        # Traverse the left subtree
        self.inorder(root.left, result)
        # Add the root's value
        result.append(root.data)
        # Traverse the right subtree
        self.inorder(root.right, result)
    
    # Function to merge two sorted arrays.
    def mergeSortedArrays(self, arr1, arr2):
        i, j = 0, 0
        merged = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        # Add the remaining elements of arr1 or arr2
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        return merged
    
    # Function to merge two BSTs.
    def merge(self, root1, root2):
        # Step 1: Perform inorder traversal of both BSTs to get sorted arrays.
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        
        # Step 2: Merge the two sorted arrays.
        return self.mergeSortedArrays(arr1, arr2)
