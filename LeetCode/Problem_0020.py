# LeetCode Problem 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        elements = ''
        for i in range(len(s)):
            elements += s[i]
            if len(elements) > 1 and s[i] in brackets:
                if elements[-2] == brackets[s[i]]:
                    elements = elements[:-2]
                else:
                    return False
        if len(elements) != 0:
            return False
        return True

        # elements = []
        # for i in range(len(s)):
        #     elements.append(s[i])
        #     if len(elements) > 1 and s[i] in brackets:
        #         if elements[-2] == brackets[s[i]]:
        #             elements.pop()
        #             elements.pop()
        #         else:
        #             return False
        # if len(elements) != 0:
        #     return False
        # return True

        # count = {('(',')'):0, ('[',']'):0, ('{','}'):0}
        # for i in range(len(s)):
        #     for key in count:
        #         if key[0] == s[i]:
        #             count[key] += 1
        #         elif key[1] == s[i]:
        #             count[key] -= 1
        #         if count[key] < 0:
        #             return False
        # return True

        # bracket = {'(':')', '[':']', '{':'}'}
        # for i in range(len(s)):
        #     if i%2 == 0:
        #         if s[i] not in bracket:
        #             return False
        #         else:
        #             if i+1 == len(s):
        #                 return False
        #             else:
        #                 if s[i+1] != bracket[s[i]]:
        #                     return False
        #     elif i%2 == 1:
        #         if i+1 == len(s):
        #             return True
