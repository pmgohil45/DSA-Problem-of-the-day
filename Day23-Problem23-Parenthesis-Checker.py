"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

Examples :
Input: {([])}
Output: true
Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.

Input: ()
Output: true
Explanation: (). Same bracket can form balanced pairs,and here only 1 type of bracket is present and in balanced way.

Input: ([]
Output: false
Explanation: ([]. Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 10^5
"""

class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the string
        for char in x:
            # If it's an opening bracket, push it onto the stack
            if char in '({[':
                stack.append(char)
            # If it's a closing bracket
            elif char in ')}]':
                # Check if stack is empty or top of stack doesn't match the current closing bracket
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                # Pop the opening bracket from the stack
                stack.pop()
        
        # If stack is empty, all brackets were balanced
        return len(stack) == 0

# Example usage
sol = Solution()
#print(sol.ispar("{([])}"))  # Output: true
#print(sol.ispar("()"))      # Output: true
#print(sol.ispar("([]"))     # Output: false
