# LeetCode Problem 92: Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur1, cur2, cur3, cur_temp1, cur_temp2 = None, head, head, None, None
        for _ in range(left-1):
            cur1 = cur2
            cur2 = cur2.next
        cur_temp1 = cur1
        cur_temp2 = cur2
        for i in range(right-left+1):
            cur3 = cur2.next
            cur2.next = cur1
            cur1 = cur2
            cur2 = cur3
        if cur_temp1:
            cur_temp1.next = cur1
        else:
            head = cur1
        cur_temp2.next = cur2
        return head

        # position = 1
        # while cur2:
        #     if position < left:
        #         cur1 = cur2
        #         cur2 = cur2.next
        #     elif position >= left and position <= right:
        #         if position == left:
        #             cur_temp1 = cur1
        #             cur_temp2 = cur2
        #         cur3 = cur2.next
        #         cur2.next = cur1
        #         cur1 = cur2
        #         cur2 = cur3
        #         if position == right:
        #             if cur_temp1:
        #                 cur_temp1.next = cur1
        #             else:
        #                 head = cur1
        #             cur_temp2.next = cur2
        #             return head
        #     position += 1
