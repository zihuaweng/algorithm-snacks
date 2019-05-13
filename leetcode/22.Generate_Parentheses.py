# https://leetcode.com/problems/generate-parentheses/
# 回溯. 逐个字符添加, 生成每一种组合.

# 一个状态需要记录的有: 当前字符串本身, 左括号数量, 右括号数量.

# 递归过程中解决:

# 如果当前右括号数量等于括号对数 n, 那么当前字符串即是一种组合, 放入解中.
# 如果当前左括号数量等于括号对数 n, 那么当前字符串后续填充满右括号, 即是一种组合.
# 如果当前左括号数量未超过 n:
# 如果左括号多于右括号, 那么此时可以添加一个左括号或右括号, 递归进入下一层
# 如果左括号不多于右括号, 那么此时只能添加一个左括号, 递归进入下一层

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return ''
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, l, r, string, res):
        if l > r:
            return
        if l == 0 and r == 0:
            res.append(string)
        if l > 0:
            self.helper(l - 1, r, string + '(', res)
        if r > 0:
            self.helper(l, r - 1, string + ')', res)
