#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        graph = collections.defaultdict(list)

        queue = [(root, 0)]
        for node, x in queue:
            if node:
                graph[x].append(node.val)
                queue.append((node.left, x - 1))
                queue.append((node.right, x + 1))

        res = []
        for x in sorted(graph):
            res.append(graph[x])

        return res
