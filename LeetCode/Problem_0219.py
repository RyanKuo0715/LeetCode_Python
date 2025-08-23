# LeetCode Problem 219: Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        checked = {}
        for i in range(len(nums)):
            if nums[i] in checked and i - checked[nums[i]] <= k:
                return True
            checked[nums[i]] = i
        return False

    # if k != 0:
    #     for i in range(len(nums)):
    #         for j in range(i+1, min(i+1+k, len(nums))):
    #             if nums[i] == nums[j]:
    #                 return True
    # return False

    # seen = {}
    # for i, n in enumerate(nums):
    #     if n in seen and i-seen[n] <= k:
    #         return True
    #     seen[n] = i
    # return False
