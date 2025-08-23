# LeetCode Problem 136: Single Number
# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1: O(n) in time and O(n) in space
        answer = set()
        for num in nums:
            if num not in answer:
                answer.add(num)
            else:
                answer.remove(num)
        return list(answer)[0]

        # # 2: O(n) in time and O(1) in space
        # xor = 0
        # for num in nums:
        #     xor = xor^num
        # return xor
