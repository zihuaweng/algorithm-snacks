# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 二叉树的中序遍历
# 遍历到最左边然后打印，再遍历右边


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return

        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
