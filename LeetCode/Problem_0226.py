# LeetCode Problem 226: Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTree_helper(root)
        return root

    def invertTree_helper(self, root):
        if not root or (not root.left and not root.right):
            pass
        else:
            self.invertTree_helper(root.left)
            self.invertTree_helper(root.right)
            root.left, root.right = root.right, root.left
