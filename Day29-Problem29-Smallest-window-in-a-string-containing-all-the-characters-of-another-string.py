"""
Given two strings s and p. Find the smallest window in the string s consisting of all the characters(including duplicates) of the string p.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 

Examples:

Input: s = "timetopractice", p = "toc"
Output: toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.

Input: s = "zoomlazapzo", p = "oza"
Output: apzo
Explanation: "apzo" is the smallest 
substring in which "oza" can be found.

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(n), n = len(p)

Constraints: 
1 ≤ |s|, |p| ≤ 10^5
"""

class Solution:
    
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(s) < len(p):
            return "-1"

        # Frequency map for characters in p
        freq_p = {}
        for char in p:
            freq_p[char] = freq_p.get(char, 0) + 1
        
        required = len(freq_p)  # Unique characters in p
        formed = 0  # Counts how many characters match in the current window
        window_counts = {}
        
        # Left and right pointers for the window
        l, r = 0, 0
        min_len = float('inf')
        start_idx = -1

        while r < len(s):
            # Add the current character to the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current character matches its required count
            if char in freq_p and window_counts[char] == freq_p[char]:
                formed += 1

            # Try to contract the window until it no longer contains all characters of p
            while l <= r and formed == required:
                char = s[l]

                # Update the minimum window if a smaller valid window is found
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_idx = l

                # Remove the character at position l from the window
                window_counts[char] -= 1
                if char in freq_p and window_counts[char] < freq_p[char]:
                    formed -= 1

                l += 1

            r += 1
        
        if start_idx == -1:
            return "-1"
        else:
            return s[start_idx:start_idx + min_len]
