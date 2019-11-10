#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

# https://leetcode.com/problems/exclusive-time-of-functions/


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        first = logs[0].split(':')
        _id, status, time = int(first[0]), first[1], int(first[2])
        stack = [_id]
        pre = time
        for log in logs[1:]:
            temp = log.split(':')
            _id, status, time = int(temp[0]), temp[1], int(temp[2])
            if status == 'start':
                if stack:
                    res[stack[-1]] += time - pre
                stack.append(_id)
                pre = time
            else:
                cur = stack.pop()
                res[_id] += time - pre + 1
                pre = time + 1
        return res