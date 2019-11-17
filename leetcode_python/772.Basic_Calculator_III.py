#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 另外两题可以使用一样的代码

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        queue = [i for i in s if i != ' ']
        queue.append(' ')  # 终止符号，不然后面计算会漏掉
        return self.helper(queue)

    def helper(self, queue):
        num = 0
        pre_sum = 0
        pre = 0
        sig = '+'
        while queue:
            # print(num, pre, pre_sum, sig)
            cur = queue.pop(0)
            if cur.isdigit():
                num = num * 10 + ord(cur) - ord('0')
            elif cur == '(':
                num = self.helper(queue)
            else:
                if sig == '+':
                    pre_sum += pre
                    pre = num
                elif sig == '-':
                    pre_sum += pre
                    pre = -num
                elif sig == '*':
                    pre *= num
                else:
                    if pre < 0:
                        pre = -(abs(pre) // num)
                    else:
                        pre //= num
                if cur == ')':
                    break
                sig = cur
                num = 0
        return pre + pre_sum

