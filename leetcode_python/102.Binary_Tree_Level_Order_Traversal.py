# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 使用queue将一层的结果推入，然后打印这一层的每一个结果时把左分支和右分支都推入。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level_res = []
            n = len(queue)
            for _ in range(n):
                num = queue.pop(0)
                level_res.append(num.val)
                if num.left:
                    queue.append(num.left)
                if num.right:
                    queue.append(num.right)
            res.append(level_res)
        return res
