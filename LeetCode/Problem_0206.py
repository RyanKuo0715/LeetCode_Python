# LeetCode Problem 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.cur = self.cur1 = self.cur2 = head
        if not self.cur:
            return self.cur
        if self.cur.next:
            self.cur = self.cur1 = self.cur.next
            self.cur2.next = None
            self.reverse(self.cur, self.cur1, self.cur2)
        return self.cur

    def reverse(self, cur, cur1, cur2):
        if not self.cur.next:
            self.cur.next = self.cur2
        else:
            self.cur1 = self.cur.next
            self.cur.next = self.cur2
            self.cur2 = self.cur
            self.cur = self.cur1
            self.reverse(self.cur, self.cur1, self.cur2)
