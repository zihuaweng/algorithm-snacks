#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.replace(' ', '')
        stack = []
        num = 0
        sig = '+'

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                num = num * 10 + ord(char) - ord('0')
            if not char.isdigit() or i == len(s) - 1:
                if sig == '+':
                    stack.append(num)
                elif sig == '-':
                    stack.append(-num)
                elif sig == '*':
                    stack.append(stack.pop() * num)
                else:
                    temp = stack.pop()
                    if temp < 0:
                        stack.append(-(abs(temp) // num))
                    else:
                        stack.append(temp // num)

                sig = char
                num = 0

        return sum(stack)


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        s = s.replace(' ', '')

        order_mp = {'+': 0, '-': 0, '*': 1, '/': 1}
        numstack, opstack = [], []
        i = 0
        s += '+'
        while i < len(s):
            if s[i].isdigit():
                tmp_num = ''
                while i < len(s) and s[i].isdigit():
                    tmp_num += s[i]
                    i += 1
                numstack.append(int(tmp_num))
            else:
                while opstack and order_mp[s[i]] <= order_mp[opstack[-1]]:
                    num2 = numstack.pop(-1)
                    num1 = numstack.pop(-1)
                    tmp_res = self.helper(num1, num2, opstack.pop(-1))
                    numstack.append(tmp_res)

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
