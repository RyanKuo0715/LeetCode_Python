# LeetCode Problem 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.depth = 1
        self.max_depth = [1]
        self.find_root(root, self.depth, self.max_depth)
        return self.max_depth[0]

    def find_root(self, node, depth, max_depth):
        if not node.left and not node.right:
            if self.depth > self.max_depth[0]:
                self.max_depth[0] = self.depth
        else:
            self.depth += 1
            if node.left:
                self.find_root(node.left, self.depth, self.max_depth)
            if node.right:
                self.find_root(node.right, self.depth, self.max_depth)
            self.depth -= 1
