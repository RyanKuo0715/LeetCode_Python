# LeetCode Problem 19: Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur1, cur2 = head, dummy
        for i in range(n):
            cur1 = cur1.next
        while cur1:
            cur1 = cur1.next
            cur2 = cur2.next
        cur2.next = cur2.next.next
        return dummy.next

        # count = 0
        # storage = {}
        # cur = head
        # while cur:
        #     count += 1
        #     storage[count] = cur
        #     cur = cur.next
        # if count - n > 0:
        #     if count-n+2 in storage:
        #         storage[count-n].next = storage[count-n+2]
        #     else:
        #         storage[count-n].next = None
        # else:
        #     if 2 in storage:
        #         head = storage[2]
        #     else:
        #         head = None
        # storage[count-n+1].next = None
        # return head
