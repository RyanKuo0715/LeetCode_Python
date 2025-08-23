# LeetCode Problem 230: Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = [k]
        self.kthSmallest_helper(root, value)
        return value[1]

    def kthSmallest_helper(self, root, value):
        if root and value[0]:
            self.kthSmallest_helper(root.left, value)
            value[0] -= 1
            if not value[0]:
                value.append(root.val)
            self.kthSmallest_helper(root.right, value)
