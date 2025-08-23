# LeetCode Problem 148: Sort List
# https://leetcode.com/problems/sort-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# slower but less memory usage
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None

        small = self.sortList(head)
        large = self.sortList(mid)

        dummy = ListNode()
        cur1, cur2, cur = small, large, dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 or cur2
        return dummy.next

# # faster but more memory usage
# from collections import defaultdict
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         d = defaultdict(list)
#         cur = head
#         while cur:
#             d[cur.val].append(cur)
#             cur = cur.next
#         new_head, cur = None, None
#         for value, nodes in sorted(d.items()):
#             for node in nodes:
#                 if not cur:
#                     new_head, cur = node, node
#                 else:
#                     cur.next = node
#                     cur = cur.next
#         if cur:
#             cur.next = None
#         return new_head
