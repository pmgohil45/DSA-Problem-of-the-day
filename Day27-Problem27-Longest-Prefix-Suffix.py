"""
Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples :

Input: str = "abab"
Output: 2
Explanation: "ab" is the longest proper prefix and suffix. 

Input: str = "aaaa"
Output: 3
Explanation: "aaa" is the longest proper prefix and suffix. 

Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 ≤ |str| ≤ 106
str contains lower case English alphabets
"""
class Solution:
    def lps(self, s):
        # Length of the input string
        n = len(s)

        # Create an array to hold the length of the longest prefix-suffix values for the string
        lps = [0] * n

        # Length of the previous longest prefix suffix
        length = 0

        # The loop starts from index 1 because the LPS value for the first character is always 0
        i = 1

        # Build the LPS array
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # The last value of the lps array contains the length of the longest proper prefix which is also a suffix
        return lps[-1]
