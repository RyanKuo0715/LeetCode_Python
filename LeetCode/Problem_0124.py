# LeetCode Problem 124: Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.maxPathSum_helper(root)
        return self.max_sum

    def maxPathSum_helper(self, root):
        if not root:
            return 0
        else:
            left = self.maxPathSum_helper(root.left)
            right = self.maxPathSum_helper(root.right)
            self.max_sum = max(self.max_sum, root.val + max(left + right, left, right, 0))
            return root.val + max(left, right, 0)
