#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num = [["", 1]], 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append(["", num])
                num = 0
            elif c == ']':
                top_num, count = stack.pop()
                stack[-1][0] += top_num * count
            else:
                stack[-1][0] += c

        return stack[-1][0]
