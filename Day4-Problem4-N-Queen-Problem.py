"""
The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard [3 1 4 2].

+-----------------------+
|     |  Q  |     |     |
+-----------------------+
|     |     |     |  Q  |
+-----------------------+
|  Q  |     |     |     |
+-----------------------+
|     |     |  Q  |     |
+-----------------------+

Examples:

Input: 1
Output: [1]
Explaination: Only one queen can be placed in the single cell available.

Input: 4
Output: [[2 4 1 3 ],[3 1 4 2 ]]
Explaination: These are the 2 possible solutions.

Expected Time Complexity: O(n!)
Expected Auxiliary Space: O(n2) 

Constraints:
1 ≤ n ≤ 10
"""
class Solution:
    def nQueen(self, n):
        def solve(row, cols, diag1, diag2, queens):
            # If we have successfully placed queens in all rows
            if row == n:
                result.append(queens[:])
                return
            
            # Try placing a queen in every column for the current row
            for col in range(n):
                if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                    # Place queen and mark the column and diagonals
                    queens.append(col + 1)
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    
                    # Move to the next row
                    solve(row + 1, cols, diag1, diag2, queens)
                    
                    # Backtrack: Remove queen and unmark the column and diagonals
                    queens.pop()
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
        
        result = []
        solve(0, set(), set(), set(), [])
        
        return result
