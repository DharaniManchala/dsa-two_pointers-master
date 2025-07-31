"""
🔁 Problem: Max Consecutive Ones III (LeetCode #1004)  
🔗 Link: https://leetcode.com/problems/max-consecutive-ones-iii/

📌 Description:
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1's in the array if you can flip at most `k` 0's.

👨‍💻 Author: Dharani Manchala  
💡 Topic: Sliding Window, Two Pointers  
🧠 Level: Medium  
🏢 Asked in: Google, Facebook, Amazon

---
Example 1:
Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: Flip 2 zeros at indices 5 and 10 to get 6 consecutive 1s.

Example 2:
Input:  nums = [0,0,1,1,1,0,0], k = 0  
Output: 3  

---

🕒 Time Complexity: O(n)  
    - Each element is visited at most twice by left and right pointers.

📦 Space Complexity: O(1)  
    - No extra space used other than a few variables.

🔄 Tags: Sliding Window, Two Pointers, Arrays
"""

class Solution:
    def longestOnes(self, nums, k):
        """
        Returns the length of the longest subarray with at most k 0s flipped to 1s.

        :param nums: List[int] - binary input array
        :param k: int - maximum number of 0s we can flip
        :return: int - maximum consecutive 1s after flipping at most k zeros
        """

        left = 0     # Left pointer of the sliding window
        max_len = 0  # Store the maximum length found
        zeros = 0    # Count of 0s in the current window

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1  # Count the 0 we may flip

            # Shrink the window until we have <= k zeros
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1  # Shrink the window

            # Update the max length
            max_len = max(max_len, right - left + 1)

        return max_len

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(solution.longestOnes(nums, k))  # Output: 6
