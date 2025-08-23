# LeetCode Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash table
        index = {}
        for i in range(len(nums)):
            if target-nums[i] in index:
                return [i, index[target-nums[i]]]
            index[nums[i]] = i

        # # pointers
        # sorted_nums = sorted(nums)
        # a = 0
        # b = len(sorted_nums)-1
        # while True:
        #     if sorted_nums[a] + sorted_nums[b] == target:
        #         r1 = nums.index(sorted_nums[a])
        #         nums.pop(r1)
        #         if nums.index(sorted_nums[b]) < r1:
        #             r2 = nums.index(sorted_nums[b])
        #         else:
        #             r2 = nums.index(sorted_nums[b])+1
        #         return [r1, r2]
        #     elif sorted_nums[a] + sorted_nums[b] < target:
        #         a += 1
        #     elif sorted_nums[a] + sorted_nums[b] > target:
        #         b -= 1

        # # brutal solution
        # sorted_nums = sorted(nums)
        # for i in range(len(sorted_nums)):
        #     for j in range(len(sorted_nums)-1-i):
        #         if sorted_nums[i] + sorted_nums[i+1+j] == target:
        #             a = nums.index(sorted_nums[i])
        #             nums.pop(a)
        #             if nums.index(sorted_nums[i+1+j]) < a:
        #                 b = nums.index(sorted_nums[i+1+j])
        #             else:
        #                 b = nums.index(sorted_nums[i+1+j])+1
        #             return [a, b]
        #         if sorted_nums[i] + sorted_nums[i+1+j] > target:
        #             break
