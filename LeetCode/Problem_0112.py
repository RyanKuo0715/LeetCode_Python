# LeetCode Problem 112: Path Sum
# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target_sum = targetSum
        self.sum = 0
        self.if_sum = False
        if root:
            self.hasPathSum_helper(root)
        return self.if_sum

    def hasPathSum_helper(self, root):
        self.sum += root.val
        if (not root.left and not root.right) and self.sum == self.target_sum:
            self.if_sum = True
        elif (root.left or root.right) and not self.if_sum:
            if root.left:
                self.hasPathSum_helper(root.left)
            if root.right:
                self.hasPathSum_helper(root.right)
        self.sum -= root.val

    # if not root:
    #     if self.sum == self.target_sum:
    #         self.if_sum = True
    # else:
    #     if not self.if_sum:
    #         self.sum += root.val
    #         if root.left and not root.right:
    #             self.hasPathSum_helper(root.left)
    #         elif not root.left and root.right:
    #             self.hasPathSum_helper(root.right)
    #         else:
    #             self.hasPathSum_helper(root.left)
    #             self.hasPathSum_helper(root.right)
    #         self.sum -= root.val

    # print(not 0)  # True
    # print(not 1)  # False
