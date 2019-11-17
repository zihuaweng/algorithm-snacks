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
