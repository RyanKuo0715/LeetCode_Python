# LeetCode Problem 67: Add Binary
# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        combine = str(int(a)+int(b))
        result = ''
        temp = 0
        for i in range(len(combine)):
            if int(combine[-(i+1)])+temp < 2:
                result = str(int(combine[-(i+1)])+temp) + result
                temp = 0
            else:
                result = str((int(combine[-(i+1)])+temp)%2) + result
                temp = (int(combine[-(i+1)])+temp)//2
        if temp > 0:
            result = str(temp) + result
        return result
