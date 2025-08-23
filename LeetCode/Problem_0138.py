# LeetCode Problem 138: Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        linked_list = None
        cur1, cur2 = head, None
        storage = {}
        while cur1:
            if cur1 not in storage:
                cur2 = Node(cur1.val)
                storage[cur1] = cur2
            if not linked_list:
                linked_list = cur2
            if cur1.next and cur1.next not in storage:
                cur2.next = Node(cur1.next.val)
                storage[cur1.next] = cur2.next
            elif cur1.next and cur1.next in storage:
                cur2.next = storage[cur1.next]
            if cur1.random and cur1.random not in storage:
                cur2.random = Node(cur1.random.val)
                storage[cur1.random] = cur2.random
            elif cur1.random and cur1.random in storage:
                cur2.random = storage[cur1.random]
            cur1, cur2 = cur1.next, cur2.next
        return linked_list
