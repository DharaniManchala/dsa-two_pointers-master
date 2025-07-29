"""
🔁 Problem: Reverse String (LeetCode #344)
🔗 Link: https://leetcode.com/problems/reverse-string/

📌 Description:
Given a character array `s`, reverse the array **in-place** using the two pointers approach.
Do not use any extra space for another array — modify the input array directly.

👨‍💻 Author: Dharani Manchala
💡 Topic: Two Pointers
🧠 Level: Easy
🏢 Asked in: Google, Amazon, Microsoft

---
Example:

Input:  s = ['h', 'e', 'l', 'l', 'o']
Output: s = ['o', 'l', 'l', 'e', 'h']
---

🕒 Time Complexity: O(n)
    - We swap each character once, visiting n/2 pairs ⇒ linear time

📦 Space Complexity: O(1)
    - No extra space used. All modifications are in-place.

🔄 Tags: Arrays, Two Pointers, In-Place Algorithms
"""


class Solution:
    def reverseString(self, s):
        """
        Reverses the input character array in-place using two pointers.

        :param s: List[str] - the character array to reverse
        :return: None - modifies the list in-place

        Example:
            s = ['a', 'b', 'c']
            reverseString(s)
            # s becomes ['c', 'b', 'a']
        """

        # Initialize two pointers
        left = 0
        right = len(s) - 1

        # Loop until pointers meet
        while left < right:
            # Swap the characters at left and right indices
            s[left], s[right] = s[right], s[left]

            # Move pointers towards the center
            left += 1
            right -= 1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_input = ['h', 'e', 'l', 'l', 'o']
    solution.reverseString(example_input)
    print(example_input)  # Output: ['o', 'l', 'l', 'e', 'h']