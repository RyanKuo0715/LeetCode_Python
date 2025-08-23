# LeetCode Problem 133: Clone Graph
# https://leetcode.com/problems/clone-graph/description/

# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        linked_list = Node(node.val)
        created_node = {node: linked_list}
        self.cloneGraph_helper(linked_list, created_node, node)
        return linked_list

    def cloneGraph_helper(self, linked_list, created_node, node):
        if node.neighbors:
            for i in range(len(node.neighbors)):
                if node.neighbors[i] not in created_node:
                    new_node = Node(node.neighbors[i].val)
                    created_node[node.neighbors[i]] = new_node
                    linked_list.neighbors.append(new_node)
                    self.cloneGraph_helper(new_node, created_node, node.neighbors[i])
                else:
                    linked_list.neighbors.append(created_node[node.neighbors[i]])
