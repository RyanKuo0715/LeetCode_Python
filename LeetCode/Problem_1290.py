# LeetCode Problem 1290: Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # process ListNode directly
        cur = head
        result = 0
        while cur:
            result *= 2
            result += cur.val
            cur = cur.next
        return result

        # # list
        # cur = head
        # lst = []
        # while cur:
        #     lst.append(cur.val)
        #     cur = cur.next
        # result = 0
        # power = 0
        # for i in range(len(lst)-1, -1, -1):
        #     result += lst[i]*(2**power)
        #     power += 1
        # return result

        # dict
        # cur = head
        # num = 0
        # digits = {}
        # while cur:
        #     if cur.val:
        #         digits[num] = cur.val
        #     num += 1
        #     cur = cur.next
        # result = 0
        # for power, digit in digits.items():
        #     result += digit*(2**(num-power-1))
        # return result
