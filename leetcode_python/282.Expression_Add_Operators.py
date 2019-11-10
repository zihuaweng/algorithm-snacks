#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(4(n-1)) [所有数字中间有n-1个空格，每个空格可以有4种可能，+-*，或者没有东西，就是相连]
# Space complexity: O()

# https://leetcode.com/problems/expression-add-operators/


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        if not num:
            return res

        self.dfs(res, num, target, '', 0, 0, 0)
        return res

    def dfs(self, res, num, target, path, cal, idx, pre_cal):
        # 终止运算
        if idx == len(num):
            if cal == target:
                res.append(path)
            return

        for i in range(idx, len(num)):
            cur = num[idx:i + 1]
            if len(cur) > 1 and cur[0] == '0':
                break
            val = int(cur)
            if idx == 0:
                self.dfs(res, num, target, path + cur, cal + val, i + 1, val)
            else:
                self.dfs(res, num, target, path + '+' + cur, cal + val, i + 1, val)
                self.dfs(res, num, target, path + '-' + cur, cal - val, i + 1, -val)
                self.dfs(res, num, target, path + '*' + cur, cal - pre_cal + pre_cal * val, i + 1, pre_cal * val)

