"""
Given a String str, reverse the string without reversing its individual words. Words are separated by dots.

Note: The last character has not been '.'. 

Examples :

Input: str = i.like.this.program.very.much
Output: much.very.program.this.like.i

Explanation: After reversing the whole string(not individual words), the input string becomes much.very.program.this.like.i
Input: str = pqr.mno

Output: mno.pqr
Explanation: After reversing the whole string , the input string becomes mno.pqr

Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 <= |str| <= 10^5
"""

class Solution:
    
    # Function to reverse words in a given string.
    def reverseWords(self, str):
        # Splitting the string by the dot separator to get individual words.
        words = str.split('.')
        
        # Reversing the list of words.
        words.reverse()
        
        # Joining the words back with a dot to form the reversed string.
        result = '.'.join(words)
        
        # Returning the reversed string.
        return result

