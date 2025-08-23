# LeetCode Problem 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one += two
            two = temp
        return one

        # 1, 0 = 1
        # 1, 1 = 2
        # 2, 1 = 3
        # 3, 2 = 5
        # 5, 3 = 8

        # # permutation and combination
        # num = 0
        # for i in range(n//2+1):
        #     a = i
        #     b = n-2*i
        #     num += (math.factorial(a+b)/(math.factorial(a)*(math.factorial(b))))
        # return int(num)
