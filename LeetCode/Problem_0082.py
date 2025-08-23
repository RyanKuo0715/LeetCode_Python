# LeetCode Problem 82: Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Optional[ListNode]: can be ListNode or None
        # https://stackoverflow.com/questions/71970937/why-do-we-use-optionallistnode

        # Jerry's Solution
        cur = head
        d = defaultdict(int)
        while cur:
            d[cur.val] += 1
            cur = cur.next
        dummy = ListNode()
        cur = dummy
        for val, count in d.items():
            if count == 1:
                cur.next = ListNode(val)
                cur = cur.next
        return dummy.next

        # # Ryan's Solution
        # cur = head
        # lst = []
        # duplicate = False
        # while cur and cur.next:
        #     if cur.val != cur.next.val:
        #         if not duplicate:
        #             lst.append(cur.val)
        #         duplicate = False
        #     elif cur.val == cur.next.val:
        #         duplicate = True
        #     cur = cur.next
        # if cur and cur.val not in lst and not duplicate:
        #     lst.append(cur.val)
        # dummy = ListNode()
        # cur = dummy
        # for val in lst:
        #     cur.next = ListNode(val)
        #     cur = cur.next
        # return dummy.next
