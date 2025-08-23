# LeetCode Problem 100: Same Tree
# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     self.if_same = [True]
    #     self.check_tree(p, q)
    #     return self.if_same[0]

    # def check_tree(self, p_check, q_check):
    #     if (not p_check and q_check) or (p_check and not q_check):
    #         self.if_same[0] = False
    #     elif p_check and q_check:
    #         if p_check.val != q_check.val:
    #             self.if_same[0] = False
    #         else:
    #             self.check_tree(p_check.left, q_check.left)
    #             self.check_tree(p_check.right, q_check.right)
