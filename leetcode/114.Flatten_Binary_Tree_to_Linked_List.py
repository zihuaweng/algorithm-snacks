# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# 首先到最右边，然后右边的结点为左边结点的右结点，去除掉左节点，
# 当前结点作为作为上一个结点递归上去。
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.previous = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
            # 先走到最右边
        self.flatten(root.right)
        # 每到一个右边处理完之后要处理这个右边的左边
        self.flatten(root.left)

        root.right = self.previous
        root.left = None

        self.previous = root
