# LeetCode Problem 191: Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n%2 != 0:
                count += 1
            n//=2
        return count
