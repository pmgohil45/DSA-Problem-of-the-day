"""
Given a Matrix mat of n*n size. Your task is constructing a 2D linked list representation of the given matrix.

Input: mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output (N = Null): 
1 → 2 → 3 → N
↓   ↓   ↓
4 → 5 → 6 → N
↓   ↓   ↓
7 → 8 → 9 → N
↓   ↓   ↓
N   N   N

Input: mat = [[23, 28], [23, 28]]
Output:
23 → 28 → N
 ↓    ↓
23 → 28 → N
 ↓    ↓
 N    N

Expected Time Complexity: O(n^2)
Expected Space Complexity: O(n^2)

Constraints:
1 <= mat.size() <= 15
1 <= mat[i][j] <= 10^4
"""
'''
class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None
'''
# Back-end complete function Template for Python 3
class Solution:

    def constructUtil(self, mat, i, j, m, n):
        # Base case: if index exceeds the matrix size, return None
        if i >= n or j >= m:
            return None

        # Create a new node with the value from the matrix
        temp = Node(mat[i][j])

        # Construct the right and down pointers recursively
        temp.right = self.constructUtil(mat, i, j + 1, m, n)
        temp.down = self.constructUtil(mat, i + 1, j, m, n)

        return temp

    def constructLinkedMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        # Call the utility function to construct the linked matrix starting from the top-left corner (0, 0)
        return self.constructUtil(mat, 0, 0, m, n)
