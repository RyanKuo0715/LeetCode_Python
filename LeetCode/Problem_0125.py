# LeetCode Problem 125: Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        return self.isPalindrome_helper(s, i, j)

    def isPalindrome_helper(self, s, i, j):
        while not s[i].isalpha() and not s[i].isdigit() and j - i > 0:
            i += 1
        while not s[j].isalpha() and not s[j].isdigit() and j - i > 0:
            j -= 1
        if j - i <= 0:
            return True
        elif s[i].lower() != s[j].lower():
            return False
        else:
            return self.isPalindrome_helper(s, i + 1, j - 1)

        # i, j = 0, len(s)-1
        # while j-i > 0:
        #     while not s[i].isalpha() and not s[i].isdigit() and j-i > 0:
        #         i += 1
        #     while not s[j].isalpha() and not s[j].isdigit() and j-i > 0:
        #         j -= 1
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i += 1
        #     j -= 1
        # return True

        # while len(s) > 1:
        #     while not s[0].isalpha() and not s[0].isdigit() and len(s) > 1:
        #         s = s[1:]
        #     while not s[-1].isalpha() and not s[-1].isdigit() and len(s) > 1:
        #         s = s[:-1]
        #     if len(s) == 0 or len(s) == 1:
        #         return True
        #     elif s[0].lower() != s[-1].lower():
        #         return False
        #     s = s[1:-1]
        # return True

        # if len(s) == 0 or len(s) == 1:
        #     return True
        # else:
        #     while not s[0].isalpha() and not s[0].isdigit() and len(s) > 1:
        #         s = s[1:]
        #     while not s[-1].isalpha() and not s[-1].isdigit() and len(s) > 1:
        #         s = s[:-1]
        #     if len(s) == 0 or len(s) == 1:
        #         return True
        #     elif s[0].lower() != s[-1].lower():
        #         return False
        #     else:
        #         return self.isPalindrome(s[1:-1])
