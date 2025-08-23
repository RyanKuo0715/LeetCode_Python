# LeetCode Problem 215: Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]

        # count, local_min, data = 0, float('inf'), []
        # for num in nums:
        #     if count < k:
        #         count += 1
        #         data.append(num)
        #         if num < local_min:
        #             local_min = num
        #     else:
        #         if num > local_min:
        #             data.remove(min(data))
        #             data.append(num)
        #             local_min = min(data)
        # return local_min
