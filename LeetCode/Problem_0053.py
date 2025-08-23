# LeetCode Problem 53: Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        total = float('-inf')
        for i in range(len(nums)):
            if nums[i] + total < nums[i]:
                total = nums[i]
            else:
                total += nums[i]
            maximum = max(maximum, total)
        return maximum
