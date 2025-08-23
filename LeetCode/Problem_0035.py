# LeetCode Problem 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums)-1
        while True:
            c = (a+b)//2
            if target < nums[c]:
                b = c-1
            elif target > nums[c]:
                a = c+1
            else:
                return c
            if a > b:
                return a
