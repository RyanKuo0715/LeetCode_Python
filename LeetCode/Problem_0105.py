# LeetCode Problem 105: Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # without list slicing
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_dict = {index: value for index, value in enumerate(preorder)}
        self.inorder_dict = {value: index for index, value in enumerate(inorder)}
        root = self.buildTree_helper(0, len(preorder)-1, 0, len(inorder))
        return root

    def buildTree_helper(self, pleft, pright, ileft, iright):
        if pleft > pright:
            return None
        value = self.preorder_dict[pleft]
        root = TreeNode(value)
        iposition = self.inorder_dict[value]
        sleft = iposition - ileft
        root.left = self.buildTree_helper(pleft+1, pleft+sleft, ileft, iposition-1)
        root.right = self.buildTree_helper(pleft+sleft+1, pright, iposition+1, iright)
        return root

    # # by list slicing
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if not preorder:
    #         return None
    #     root = TreeNode(preorder[0])
    #     position = inorder.index(preorder[0])
    #     root.left = self.buildTree(preorder[1:position+1], inorder[:position])
    #     root.right = self.buildTree(preorder[position+1:], inorder[position+1:])
    #     return root
