# https://leetcode.com/problems/validate-binary-search-tree/
# 判断是否正常就得到中序遍历的结果，看是不是递增的，如果不是False

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.helper(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def helper(self, root, res):
        if root is None:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
