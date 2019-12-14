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


# https://leetcode.com/problems/basic-calculator-iii/discuss/202979/A-generic-solution-for-Basic-Calculator-I-II-III
# 通用方法
# 但是需要处理负数问题

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        # remove the space and correct negative integers.
        s = s.replace(' ', '')
        for i in range(len(s)):
            if s[i] == '-' and (i == 0 or s[i - 1] == '('):
                s = s[:i] + '0' + s[i:]

        order_mp = {'+': 0, '-': 0, '*': 1, '/': 1, ')': -1}
        numstack, opstack = [], []
        i = 0
        s += '+'
        while i < len(s):
            if s[i] == '(':
                opstack.append(s[i])
                i += 1
            elif s[i].isdigit():
                tmp_num = ''
                while i < len(s) and s[i].isdigit():
                    tmp_num += s[i]
                    i += 1
                numstack.append(int(tmp_num))
            else:
                while opstack and opstack[-1] != '(' and order_mp[s[i]] <= order_mp[opstack[-1]]:
                    num2 = numstack.pop(-1)
                    num1 = numstack.pop(-1)
                    tmp_res = self.helper(num1, num2, opstack.pop(-1))
                    numstack.append(tmp_res)

                if s[i] == ')':
                    opstack.pop(-1)
                else:
                    opstack.append(s[i])
                i += 1
        return numstack[0]

    def helper(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        else:
            return n1 // n2
