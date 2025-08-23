# LeetCode Problem 189: Rotate Array
# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    # # slow
    # def rotate(self, nums: List[int], k: int) -> None:
    #     k %= len(nums)
    #     for i in range(k):
    #         a = nums.pop()
    #         nums.insert(0, a)

    # # faster than above but still slow
    # def rotate(self, nums: List[int], k: int) -> None:
    #     k %= len(nums)
    #     for i in range(len(nums)-k):
    #         a = nums.pop(0)
    #         nums.append(a)
