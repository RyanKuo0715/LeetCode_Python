# LeetCode Problem 141: Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked_list = head
        cur = head
        element = set()
        while cur:
            if cur.next in element:
                return True
            element.add(cur.next)
            cur = cur.next
        return False

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     linked_list = head
    #     cur = head
    #     while cur:
    #         if cur.next:
    #             if not isinstance(cur.next.val, int):
    #                 return True
    #         cur.val = str(cur.val)
    #         cur = cur.next
    #     return False
