# LeetCode Problem 23: Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data = defaultdict(int)
        for lst in lists:
            cur = lst if lst else None
            while cur:
                data[cur.val] += 1
                cur = cur.next
        dummy = ListNode()
        cur = dummy
        if data:
            for node, num in sorted(data.items()):
                for i in range(num):
                    cur.next = ListNode(node)
                    cur = cur.next
        return dummy.next
