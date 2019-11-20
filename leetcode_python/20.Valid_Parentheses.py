# https://leetcode.com/problems/valid-parentheses/
# 设置一个stack，每次判断stack最后一个元素是否和新入的元素匹配，匹配pop，否则return false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last == '(' and c == ')':
                    continue
                if last == '{' and c == '}':
                    continue
                if last == '[' and c == ']':
                    continue
                return False

        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        p = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in p.values():
                stack.append(char)
            else:
                if not stack or p[char] != stack.pop():
                    return False
            # print(stack)

        return not stack

