#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        path sum = max(0, sum(root.left)) + root.val + max(0, sum(root.right))
        
        cur node works as a child node and return
            cur .val + max(0, sum(cur.left), sum(cur.right))


           -10
           / \
          9  20
            /  \
           15   7   


           -10
           / \
          9  42  

        cur_max = 42 | 41
        
        test case &corner case:
            1
            
            
        time O(n)
        space O(1)
        """
        self.max_sum = float('-inf')
        if not root:
            return self.max_sum
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        cur = node.val + left + right
        self.max_sum = max(self.max_sum, cur)
        return node.val + max(left, right)
