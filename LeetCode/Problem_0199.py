# LeetCode Problem 199: Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        processing = [root, 0]
        while len(processing) > 1:
            node = processing.pop(0)
            if node is 0:
                result.append(value)
                processing.append(0)
            else:
                value = node.val
                if node.left:
                    processing.append(node.left)
                if node.right:
                    processing.append(node.right)
        result.append(value)
        return result
