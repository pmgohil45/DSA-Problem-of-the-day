"""
Given a string str consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:
  • For every opening parenthesis, there is a closing parenthesis.
  • Opening parenthesis must be closed in the correct order.

Examples :
• Input: str = ((()
  Output: 2
  Explaination: The longest valid parenthesis substring is "()".

• Input: str = )()())
  Output: 4
  Explaination: The longest valid parenthesis substring is "()()".

Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 ≤ |str| ≤ 10^5  
"""

class Solution:
    def maxLength(self, str: str) -> int:
        stack = [-1]
        max_len = 0

        for i, char in enumerate(str):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

# Example usage
sol = Solution()

# Example 1
str1 = "((()"
#print(sol.maxLength(str1))  # Output: 2

# Example 2
str2 = ")()())"
#print(sol.maxLength(str2))  # Output: 4
