"""
Problem: Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Approach:
- Use sliding window with a frequency map
- Keep track of the count of the most frequent character
- If (window length - max frequency) > k, shrink window
- Otherwise, expand window
- Track max length of valid window

Time Complexity: O(n), where n is length of the string
Space Complexity: O(26) = O(1), fixed alphabet size

Author: Dharani Manchala
Date: 2025-07-29
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        max_freq = 0
        count = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement("AABABBA", 1))  # Output: 4
    print(solution.characterReplacement("ABAB", 2))     # Output: 4
    print(solution.characterReplacement("AABBA", 1))    # Output: 4